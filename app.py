from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import sys
import os

# Install dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Start Streamlit
subprocess.Popen([
    "streamlit", 
    "run", 
    "frontend/app.py",
    "--server.port=8501",
    "--server.address=0.0.0.0"
])

# Simple proxy server
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        import urllib.request
        try:
            with urllib.request.urlopen(f"http://localhost:8501{self.path}") as response:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(502, str(e))
    
    def do_POST(self):
        import urllib.request
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        req = urllib.request.Request(f"http://localhost:8501{self.path}", data=post_data)
        try:
            with urllib.request.urlopen(req) as response:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(502, str(e))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Serving on port {port}")
    server.serve_forever()
