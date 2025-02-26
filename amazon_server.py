from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import logging

# Amazon book link
AMAZON_LINK = "https://www.amazon.com/dp/B0DXLK1CYQ"

# Set up logging
logging.basicConfig(filename="amazon_visits.log", level=logging.INFO, format="%(asctime)s - %(message)s")

class AmazonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract client IP correctly (avoiding 127.0.0.1)
        client_ip = self.headers.get('X-Forwarded-For', self.client_address[0])

        # Log visit details
        logging.info(f"Visitor IP: {client_ip} | User-Agent: {self.headers.get('User-Agent')} | Referrer: {self.headers.get('Referer')}")

        # Serve the landing page
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(open("amazon_landing.html", "rb").read())

# Start the server
PORT = 8080
server = HTTPServer(("", PORT), AmazonHandler)
print(f"🚀 Server running at http://localhost:{PORT}")
server.serve_forever()
