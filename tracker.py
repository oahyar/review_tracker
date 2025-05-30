from flask import Flask, request, redirect
from datetime import datetime
from pytz import timezone
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Your Google Review URL
FINAL_URL = "https://www.google.com/search?client=mobilesearchapp&bih=902&biw=440&channel=iss&cs=1&hl=en_GB&rlz=1MDAPLA_en-GBSG1144SG1144&sca_esv=b5608bee10f15177&v=365.1.750410080&q=mr.onigiri+reviews&uds=ABqPDvzcTwq5-in_dnt8e-Dss_W8Q-HIurtpRY-Alh3XIQF-DDW33KzB0RhAEUcqufFHimcW_6Syb8zz_v727Oh-Pk60KCuJuZeK6kBnt16keqrHBRCRhgDI6hyFn0nFO5EP0KbLT9ExnReuJWODWI9NcassKnhgCFiEVsZ9_2-BYU5T-hbiuzyhKcr0ycXwg8Jxlfc2ZLbj-DW-WVIJXnXCtbYkN5Q0s0qwXd4Y8oFxDaqJVNTr_sUktJ62pG84_YXgd68UY7ooGlXRHawYbuelqeyDbOgSMT6vefTmDGzN-b_2RPjPbU-J_IVGtX24RyurF8yuwhs66L6Gi842IFcEr90gyyFzoadqJPtqdl3xHNHUdD3WxpYyrC2NEHP1LShqLE2JQ4Ggd8fvONBxM52gV4aIwk8P_w&si=APYL9bs7Hg2KMLB-4tSoTdxuOx8BdRvHbByC_AuVpNyh0x2KzeTOyxxXd_-EJ5U6UrhtRTGqXRTIrj1tIMfYI06NUruw1bMTbO7gI5iptkiXRe2pK07eq3AD4dJf-0KX96LHxvhePcMc&sa=X&ved=2ahUKEwjTpOaO0fWMAxWfbGwGHS4GLxEQk8gLegQIGxAB&ictx=1"

# Setup Google Sheets access
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open the sheet (use exact sheet name)
sheet = client.open("ReviewTrackerLog").sheet1

@app.route('/track')
def track():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    sg = timezone('Asia/Singapore')
    timestamp = datetime.now(sg).strftime("%Y-%m-%d %H:%M:%S")

    # Append to sheet
    method = request.method
    path = request.path
    sheet.append_row([timestamp, ip, user_agent, method, path])

    # Redirect to final destination
    return redirect(FINAL_URL)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)