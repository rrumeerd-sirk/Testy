#!/usr/bin/env python3
import http.server
import socketserver
import sys

class LargeFileHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='/home/delta/gh/testy', **kwargs)
    
    def copyfile(self, source, outputfile):
        # Use larger buffer for large files
        shutil.copyfileobj(source, outputfile, length=65536)
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

import shutil
PORT = 8000
with socketserver.TCPServer(("", PORT), LargeFileHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
