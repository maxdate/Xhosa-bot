
import os
from flask import Flask, request
app = Flask(__name__)
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "xhosa123")
WA_TOKEN = os.getenv("WA_TOKEN")
PHONE_ID = os.getenv("PHONE_ID")
@app.route("/")
def home():
    return "Xhosa bot is live!"
@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Forbidden", 403
@app.route("/webhook", methods=["POST"])
def webhook():
    return "ok", 200
