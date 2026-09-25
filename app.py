import os, requests
from flask import Flask, request
app = Flask(__name__)
HF_TOKEN=os.getenv("HF_TOKEN")
PHONE_ID=os.getenv("PHONE_ID")
WA_TOKEN=os.getenv("WA_TOKEN")
MODEL="Helsinki-NLP/opus-mt-en-xh"
def translate(t):
 try:
  r=requests.post(f"https://api-inference.huggingface.co/models/{MODEL}",headers={"Authorization":f"Bearer {HF_TOKEN}"},json={"inputs":t},timeout=30)
  return r.json()[0]['translation_text']
 except: return "Ndiyaxolisa, zama kwakhona"
def send(to,msg):
 requests.post(f"https://graph.facebook.com/v21.0/{PHONE_ID}/messages",headers={"Authorization":f"Bearer {WA_TOKEN}"},json={"messaging_product":"whatsapp","to":to,"text":{"body":msg}})
@app.route("/webhook",methods=["GET"])
def verify():
 if request.args.get("hub.verify_token")=="xhosa123": return request.args.get("hub.challenge")
 return "ok"
@app.route("/webhook",methods=["POST"])
def hook():
 d=request.get_json()
 try:
  m=d['entry'][0]['changes'][0]['value']['messages'][0]
  send(m['from'],translate(m['text']['body']))
 except: pass
 return "ok"
if __name__=="__main__": app.run(host="0.0.0.0",port=8000)
