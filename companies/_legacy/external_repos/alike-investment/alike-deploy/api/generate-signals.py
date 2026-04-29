from http.server import BaseHTTPRequestHandler
import json
import os
import urllib.request
import urllib.error

CLAUDE_API_URL = 'https://api.anthropic.com/v1/messages'
MODEL_OPUS = 'claude-opus-4-20250514'


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

        company = body.get('company', '')
        dimensions = body.get('dimensions', [])

        if not company:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': 'Missing company'}).encode())
            return

        # Load vault context from bundled data
        context = ''
        ctx_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'context', f'{company}.txt')
        if os.path.exists(ctx_path):
            try:
                with open(ctx_path, encoding='utf-8') as f:
                    context = f.read()
            except Exception:
                pass

        # Load schema
        schema = ''
        schema_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'schema.json')
        if os.path.exists(schema_path):
            try:
                with open(schema_path, encoding='utf-8') as f:
                    schema = f.read()
            except Exception:
                pass

        # Load calibration patterns
        calibration = ''
        cal_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'calibration.json')
        if os.path.exists(cal_path):
            try:
                with open(cal_path, encoding='utf-8') as f:
                    calibration = f.read()
            except Exception:
                pass

        dim_filter = ''
        if dimensions:
            dim_filter = f"\n重点分析以下维度: {', '.join(dimensions)}"

        system_prompt = f"""你是Alike Investment的信号分析引擎。基于公司研究材料，生成结构化的投资信号评分。

{f'Data Infra Schema: {schema}' if schema else ''}
{f'Calibration Patterns: {calibration}' if calibration else ''}

公司研究材料:
{context[:80000] if context else '(无可用材料，请基于web search获取信息)'}
{dim_filter}

要求:
1. 对每个维度(fundamental, org, leadership, exec-voice, employee, red-team, intel)生成信号
2. 每个信号包含: dimension, signal_type, title, summary, confidence(S1-S5), sentiment(positive/negative/neutral), evidence
3. 使用web search补充最新信息
4. 输出JSON格式: {{"signals": [...], "meta": {{"company": "...", "generated_at": "...", "search_rounds": N}}}}
5. 用中文输出信号内容，关键术语英文"""

        user_message = f'请对{company}公司生成全维度投资信号分析。确保每个维度至少有2-3个信号。'

        # Build Claude API request with streaming
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': api_key,
            'anthropic-version': '2023-06-01',
        }

        # Use Opus with web search and tool-use loop
        messages = [{'role': 'user', 'content': user_message}]
        tools = [{'type': 'web_search_20250305', 'name': 'web_search', 'max_uses': 30}]

        # Send SSE response
        self.send_response(200)
        self.send_header('Content-Type', 'text/event-stream')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        def send_progress(status, message):
            sse = f"data: {json.dumps({'type': 'progress', 'status': status, 'message': message})}\n\n"
            self.wfile.write(sse.encode('utf-8'))
            self.wfile.flush()

        send_progress('started', f'开始分析 {company}...')

        MAX_ROUNDS = 15
        all_text = []

        for round_num in range(MAX_ROUNDS):
            claude_body = {
                'model': MODEL_OPUS,
                'max_tokens': 16384,
                'system': system_prompt,
                'messages': messages,
                'tools': tools,
            }

            data = json.dumps(claude_body).encode('utf-8')
            req = urllib.request.Request(CLAUDE_API_URL, data=data, headers=headers, method='POST')

            try:
                with urllib.request.urlopen(req, timeout=600) as resp:
                    result = json.loads(resp.read().decode('utf-8'))
            except urllib.error.HTTPError as e:
                error_body = e.read().decode('utf-8') if e.readable() else str(e)
                send_progress('error', f'Claude API error: {error_body}')
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
                return
            except Exception as e:
                send_progress('error', str(e))
                self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
                return

            stop_reason = result.get('stop_reason', 'end_turn')
            content = result.get('content', [])

            # Count searches and collect text
            search_count = sum(1 for b in content if b.get('type') == 'server_tool_use')
            for block in content:
                if block.get('type') == 'text' and block.get('text', '').strip():
                    all_text.append(block['text'])

            if search_count > 0:
                send_progress('searching', f'Web search第{round_num+1}轮 ({search_count}次搜索)...')

            # If done, send final result
            if stop_reason == 'end_turn':
                final_text = '\n'.join(all_text)
                sse = f"data: {json.dumps({'type': 'result', 'text': final_text})}\n\n"
                self.wfile.write(sse.encode('utf-8'))
                self.wfile.flush()
                break

            # Continue conversation
            messages.append({'role': 'assistant', 'content': content})

            # Trim if messages get too large
            total_size = len(json.dumps(messages, ensure_ascii=False))
            if total_size > 500000:
                for msg in messages:
                    if msg.get('role') == 'assistant' and isinstance(msg.get('content'), list):
                        trimmed = []
                        for block in msg['content']:
                            if block.get('type') in ('text', 'server_tool_use'):
                                trimmed.append(block)
                        msg['content'] = trimmed

        send_progress('done', f'分析完成 (共{round_num+1}轮)')
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()
