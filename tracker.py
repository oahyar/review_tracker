from flask import Flask, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

# Replace with your actual Google Review URL
FINAL_URL = "https://www.google.com/search?client=mobilesearchapp&bih=902&biw=440&channel=iss&cs=1&hl=en_GB&rlz=1MDAPLA_en-GBSG1144SG1144&sca_esv=b5608bee10f15177&v=365.1.750410080&q=mr.onigiri+reviews&uds=ABqPDvzcTwq5-in_dnt8e-Dss_W8Q-HIurtpRY-Alh3XIQF-DDW33KzB0RhAEUcqufFHimcW_6Syb8zz_v727Oh-Pk60KCuJuZeK6kBnt16keqrHBRCRhgDI6hyFn0nFO5EP0KbLT9ExnReuJWODWI9NcassKnhgCFiEVsZ9_2-BYU5T-hbiuzyhKcr0ycXwg8Jxlfc2ZLbj-DW-WVIJXnXCtbYkN5Q0s0qwXd4Y8oFxDaqJVNTr_sUktJ62pG84_YXgd68UY7ooGlXRHawYbuelqeyDbOgSMT6vefTmDGzN-b_2RPjPbU-J_IVGtX24RyurF8yuwhs66L6Gi842IFcEr90gyyFzoadqJPtqdl3xHNHUdD3WxpYyrC2NEHP1LShqLE2JQ4Ggd8fvONBxM52gV4aIwk8P_w&si=APYL9bs7Hg2KMLB-4tSoTdxuOx8BdRvHbByC_AuVpNyh0x2KzeTOyxxXd_-EJ5U6UrhtRTGqXRTIrj1tIMfYI06NUruw1bMTbO7gI5iptkiXRe2pK07eq3AD4dJf-0KX96LHxvhePcMc&sa=X&ved=2ahUKEwjTpOaO0fWMAxWfbGwGHS4GLxEQk8gLegQIGxAB&ictx=1"

@app.route('/track')
def track():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("log.txt", "a") as f:
        f.write(f"{timestamp} | IP: {ip} | UA: {user_agent}\n")

    return redirect(FINAL_URL)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
