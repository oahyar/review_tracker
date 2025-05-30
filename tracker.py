from flask import Flask, request, redirect
from datetime import datetime
from pytz import timezone
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets setup (same as before)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("ReviewTrackerLog").sheet1

@app.route('/track')
def track():
    # Get review URL from query parameter
    final_url = request.args.get("to")
    if not final_url:
        return "Missing 'to' parameter", 400

    # Get tracking info
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    sg = timezone('Asia/Singapore')
    timestamp = datetime.now(sg).strftime("%Y-%m-%d %H:%M:%S")

    # Log it
    sheet.append_row([timestamp, ip, user_agent, final_url])

    # Redirect
    return redirect(final_url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
