import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = int(os.environ.get("PORT", 8000))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

with HTTPServer(("", port), Handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
