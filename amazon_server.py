from flask import Flask, request, redirect

app = Flask(__name__)

# Amazon product link (replace with yours)
AMAZON_URL = "https://www.amazon.com/dp/B0DXLK1CYQ"

@app.route("/")
def track():
    visitor_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent", "Unknown")
    referrer = request.headers.get("Referer", "Direct Visit")

    # Log visitor data (store in a local text file)
    with open("logs.txt", "a") as log:
        log.write(f"IP: {visitor_ip} | Agent: {user_agent} | Referrer: {referrer}\n")

    # Redirect to Amazon
    return redirect(AMAZON_URL, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
