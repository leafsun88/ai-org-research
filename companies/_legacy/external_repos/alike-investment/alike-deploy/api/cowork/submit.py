from http.server import BaseHTTPRequestHandler
import json
import os

PENDING_FILE = '/tmp/cowork_pending.json'


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length).decode('utf-8')) if length > 0 else {}

        # In production on Vercel, this is essentially a no-op
        # In dev mode, write to /tmp for Claude Code to pick up
        is_vercel = os.environ.get('VERCEL', '')
        if is_vercel:
            # Production: acknowledge but don't persist (would need KV store)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                'ok': True,
                'message': 'Cowork submit received (production mode - no persistent storage)',
            }).encode())
            return

        # Dev mode: write to tmp file
        try:
            with open(PENDING_FILE, 'w') as f:
                json.dump(body, f, ensure_ascii=False)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': str(e)}).encode())
