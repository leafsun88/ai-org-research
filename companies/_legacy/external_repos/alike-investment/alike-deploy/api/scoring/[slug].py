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
        # Extract slug from path: /api/scoring/{slug}
        path = urlparse(self.path).path
        slug = path.rstrip('/').split('/')[-1]

        if not slug:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': 'Missing slug'}).encode())
            return

        data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'scoring', f'{slug}.json')
        try:
            with open(data_path, encoding='utf-8') as f:
                bundle = json.load(f)
            # Return signal_engine as the main data (frontend expects this format)
            scoring_data = bundle.get('signal_engine', bundle)
            # Attach dim_analysis if available
            if bundle.get('dim_analysis'):
                scoring_data['dim_analysis'] = bundle['dim_analysis']
            body = json.dumps({'ok': True, 'data': scoring_data}, ensure_ascii=False)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(body.encode('utf-8'))
        except FileNotFoundError:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': f'No scoring data for {slug}'}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'ok': False, 'error': str(e)}).encode())
