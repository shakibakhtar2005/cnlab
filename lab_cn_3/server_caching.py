import http.server
import socketserver
import hashlib
import os
import time
from email.utils import formatdate, parsedate_to_datetime

PORT = 8080
FILE_PATH = "index.html"

class CachingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = FILE_PATH
        
        # Compute ETag (MD5 hash of file)
        with open(FILE_PATH, "rb") as f:
            file_content = f.read()
        etag = hashlib.md5(file_content).hexdigest()
        
        # Last modified time
        last_modified = formatdate(os.path.getmtime(FILE_PATH), usegmt=True)
        
        # Check client headers
        client_etag = self.headers.get("If-None-Match")
        client_modified = self.headers.get("If-Modified-Since")

        not_modified = False
        if client_etag == etag:
            not_modified = True
        elif client_modified:
            client_time = parsedate_to_datetime(client_modified)
            file_time = parsedate_to_datetime(last_modified)
            if client_time >= file_time:
                not_modified = True

        if not_modified:
            self.send_response(304)  # Not Modified
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("ETag", etag)
            self.send_header("Last-Modified", last_modified)
            self.end_headers()
            self.wfile.write(file_content)

with socketserver.TCPServer(("", PORT), CachingHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
