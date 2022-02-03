# coding=utf-8
# !flask/bin/python
from flask import Flask
from flask import request
import json
import os

app = Flask(__name__)

msgs = []

@app.route('/requests')
def index():
    return {"messages":msgs}


#@app.route("/*", methods=['POST'])
@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def sms(path):
    global msgs
    sms_request = request.json
    # from_=str(sms_request["from"])
    # to=str(sms_request["to"])
    # body=str(sms_request["body"])
    # msgs.append((from_,to,body))
    msgs.append(sms_request)
    if len(msgs)>10:
        msgs = msgs[-10:]
    print("Mock OTP service: sending sms body: %s"%(sms_request))
    return """{"status":"OK"}"""


if __name__ == '__main__':
    app.run(debug=os.getenv("API_DEBUG", False), port=os.getenv("API_PORT", "8765"), host=os.getenv("API_HOST", "0.0.0.0"))
