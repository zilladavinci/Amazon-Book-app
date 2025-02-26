from flask import Flask, request, redirect
import logging

app = Flask(__name__)

# Setup Logging
logging.basicConfig(filename="visitor_logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Amazon Redirect Link
AMAZON_LINK = "https://www.amazon.com/dp/B0DXLK1CYQ"

@app.route('/')
def track_and_redirect():
    visitor_ip = request.remote_addr  # Get IP Address
    user_agent = request.headers.get('User-Agent', 'Unknown')  # Get User-Agent
    referrer = request.referrer or "Direct Visit"  # Get Referrer (if available)

    # Log the visitor details
    log_entry = f"IP: {visitor_ip} | Referrer: {referrer} | User-Agent: {user_agent}"
    app.logger.info(log_entry)

    return redirect(AMAZON_LINK)  # Redirect to Amazon

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render default port
