import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    # We don't want to reply to ourselves!
    if data['name'] != 'groupme-reply-bot':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg, data['id'])

    return "ok", 200

@app.route('/', methods=['GET'])
def ping():
    return "ok", 200

def send_message(msg, reply_id):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id' : 'ace37a9b6490274c052902a3d0',
          'text'   : msg,
          'attachments':
          {
            'type': 'reply',
            'reply_id': reply_id,
            'base_reply_id': reply_id
          }
         }
    request = Request(url, urlencode(data).encode())
    print(request.text)
    json = urlopen(request).read().decode()
