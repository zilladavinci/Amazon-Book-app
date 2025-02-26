from flask import Flask, request, redirect
import logging
import requests
import json

app = Flask(__name__)

# Amazon book link
AMAZON_LINK = "https://www.amazon.com/dp/B0DXLK1CYQ"

# Configure logging to save visitor data
LOG_FILE = "visitor_logs.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def get_geo_info(ip):
    """
    Fetches geolocation data for a given IP using a free API.
    Returns city, region, country, and ISP details.
    """
    if ip == "127.0.0.1":  # Skip local IP logging
        return "Localhost - No Geo Data"
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,query")
        data = response.json()
        if data["status"] == "success":
            return f"{data['city']}, {data['regionName']}, {data['country']} | ISP: {data['isp']}"
        else:
            return "Geo Lookup Failed"
    except:
        return "Geo API Error"

@app.route('/')
def track_visitor():
    visitor_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    referrer = request.referrer if request.referrer else "Direct Visit"
    geo_info = get_geo_info(visitor_ip)
    
    log_message = f"IP: {visitor_ip} | Location: {geo_info} | User-Agent: {user_agent} | Referrer: {referrer}"
    
    # Save to log file
    logging.info(log_message)
    
    # Print to console for real-time monitoring
    print(log_message)
    
    # Redirect user to Amazon link
    return redirect(AMAZON_LINK)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging to store visitor data in logs.txt
logging.basicConfig(filename="logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

@app.route("/")
def track():
    # Get real visitor IP (fixes 127.0.0.1 issue)
    visitor_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent", "Unknown")
    referrer = request.headers.get("Referer", "Direct Visit")

    # Log visitor info
    log_entry = f"IP: {visitor_ip} | Agent: {user_agent} | Referrer: {referrer}"
    logging.info(log_entry)
    print(log_entry)

    return "✅ Tracking Active", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

