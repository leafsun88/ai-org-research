from http.server import BaseHTTPRequestHandler
import json
import os
from urllib.parse import urlparse


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        # Extract slug from path: /api/artifacts/{slug}
        path = urlparse(self.path).path
        slug = path.rstrip('/').split('/')[-1]

        if not slug:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': 'Missing slug'}).encode())
            return

        data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'artifacts', f'{slug}.json')
        try:
            with open(data_path, encoding='utf-8') as f:
                data = json.load(f)
            body = json.dumps({'ok': True, 'artifacts': data}, ensure_ascii=False)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(body.encode('utf-8'))
        except FileNotFoundError:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'artifacts': {}}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': str(e)}).encode())
