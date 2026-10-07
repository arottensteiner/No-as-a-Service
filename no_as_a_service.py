"""No-as-a-Service (NaaS): a tiny HTTP API that always answers "No".

Uses only the Python standard library.

Usage:
    python no_as_a_service.py            # listens on 0.0.0.0:8000
    python no_as_a_service.py 5000       # custom port

Endpoints (GET only):
    /        ->  No
    /<any>   ->  No
    /docs    ->  this documentation

Query it:
    curl http://localhost:8000/
    curl http://localhost:8000/docs
"""

import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
DEFAULT_PORT = 8000
ANSWER = "No"


class NoHandler(BaseHTTPRequestHandler):
    """Responds to GET /docs with the usage docs, and to any other path with "No"."""

    def do_GET(self):
        text = __doc__ if self.path.rstrip("/") == "/docs" else ANSWER
        body = (text.strip() + "\n").encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    server = HTTPServer((HOST, port), NoHandler)
    print(f"No-as-a-Service listening on http://{HOST}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down. (No.)")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
