#!/usr/bin/python3

import json
import http.server

"""
Cotain the class for check the server with a little API
"""


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    """
    Contain the functionnement of API
    """

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            json_bytes = json.dumps(json_data).encode("utf-8")
            self.wfile.write(json_bytes)
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000


with http.server.HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
