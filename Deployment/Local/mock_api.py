#!/usr/bin/env python3
"""Mock API server for local validation.

Receives the POSTs sent by the ESP32 firmware (Fase 1) and prints the
JSON body to the console. Useful while the real Spring Boot API (Fase 2)
does not exist yet.

Usage:
    python3 Deployment/Local/mock_api.py [port]
"""
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = body.decode("utf-8", errors="replace")

        print(json.dumps({"path": self.path, "body": data}, ensure_ascii=False))
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "ok"}')

    def log_message(self, fmt, *args):
        sys.stderr.write("[mock] %s\n" % (fmt % args))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"[mock] listening on 0.0.0.0:{port} (POST /readings)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
