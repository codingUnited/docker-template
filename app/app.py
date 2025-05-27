# app/app.py
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# Get environment variables or use defaults
app_name = os.environ.get("APP_NAME", "Simple App")
greeting = os.environ.get("GREETING_MESSAGE", "Hello from a basic Python server!")
port = int(os.environ.get("PORT", 8000)) # Dockerfile EXPOSEs 8000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = f"<html><head><title>{app_name}</title></head>"
        message += f"<body><h1>{greeting}</h1>"
        message += f"<p>This is a simple Python HTTP server running inside a Docker container.</p>"
        message += f"<p>Application Name: {app_name}</p>"
        message += "</body></html>"
        self.wfile.write(bytes(message, "utf8"))

def run(server_class=HTTPServer, handler_class=SimpleHandler, server_port=port):
    server_address = ('', server_port) # Listen on all available interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {server_port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
