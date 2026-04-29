from http.server import BaseHTTPRequestHandler
import json
import os
import urllib.request
import urllib.error

CLAUDE_API_URL = 'https://api.anthropic.com/v1/messages'
MODEL = 'claude-sonnet-4-20250514'


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        api_key = os.environ.get('ANTHROPIC_API_KEY', '')
        if not api_key:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': 'ANTHROPIC_API_KEY not configured'}).encode())
            return

        # Parse request body
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length).decode('utf-8')) if length > 0 else {}

        user_message = body.get('message', '')
        company = body.get('company', '')
        history = body.get('history', [])
        web_search = body.get('web_search', False)

        if not user_message:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': 'Missing message'}).encode())
            return

        # Load company context from bundled data if available
        context = ''
        if company:
            ctx_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'context', f'{company}.txt')
            if os.path.exists(ctx_path):
                try:
                    with open(ctx_path, encoding='utf-8') as f:
                        context = f.read()
                except Exception:
                    pass

        system_prompt = f"""你是Alike Investment的AI研究助手。你帮助投资者分析公司、评估投资机会。

用中文回答，关键术语保留英文。回答要有结构、有论据、有结论。

{'公司研究材料：' + context[:60000] if context else ''}"""

        # Build messages with history
        messages = []
        if history:
            for h in history:
                role = h.get('role', 'user')
                content = h.get('content', '')
                if role in ('user', 'assistant') and content.strip():
                    messages.append({'role': role, 'content': content})
        messages.append({'role': 'user', 'content': user_message})

        # Ensure messages alternate roles
        cleaned = []
        for m in messages:
            if cleaned and cleaned[-1]['role'] == m['role']:
                cleaned[-1]['content'] += '\n' + m['content']
            else:
                cleaned.append(m)
        if cleaned and cleaned[0]['role'] != 'user':
            cleaned = cleaned[1:]

        # Build Claude API request
        claude_body = {
            'model': MODEL,
            'max_tokens': 8192,
            'stream': True,
            'system': system_prompt,
            'messages': cleaned,
        }
        if web_search:
            claude_body['tools'] = [{'type': 'web_search_20250305', 'name': 'web_search'}]

        data = json.dumps(claude_body).encode('utf-8')
        req = urllib.request.Request(
            CLAUDE_API_URL,
            data=data,
            headers={
                'Content-Type': 'application/json',
                'x-api-key': api_key,
                'anthropic-version': '2023-06-01',
            },
            method='POST',
        )

        # Send SSE response
        self.send_response(200)
        self.send_header('Content-Type', 'text/event-stream')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                buffer = b''
                while True:
                    chunk = resp.read(1024)
                    if not chunk:
                        break
                    buffer += chunk
                    # Parse SSE events from Claude's streaming response
                    while b'\n\n' in buffer:
                        event_data, buffer = buffer.split(b'\n\n', 1)
                        for line in event_data.decode('utf-8').split('\n'):
                            if line.startswith('data: '):
                                try:
                                    evt = json.loads(line[6:])
                                    evt_type = evt.get('type', '')
                                    if evt_type == 'content_block_delta':
                                        delta = evt.get('delta', {})
                                        if delta.get('type') == 'text_delta':
                                            text = delta.get('text', '')
                                            sse = f"data: {json.dumps({'text': text})}\n\n"
                                            self.wfile.write(sse.encode('utf-8'))
                                            self.wfile.flush()
                                except (json.JSONDecodeError, KeyError):
                                    pass

            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
        except Exception as e:
            err_msg = f"data: {json.dumps({'error': str(e)})}\n\ndata: [DONE]\n\n"
            self.wfile.write(err_msg.encode('utf-8'))
            self.wfile.flush()
