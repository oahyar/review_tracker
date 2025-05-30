from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

# Replace with your actual Google Review URL
FINAL_URL = "https://g.page/r/YOUR_REVIEW_LINK"

@app.route('/track')
def track():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a") as f:
        f.write(f"{timestamp} | IP: {ip} | UA: {user_agent}\n")

    return redirect(FINAL_URL)

if __name__ == "__main__":
    app.run()
