import os

from flask import Flask, abort, request
from wechatpy import create_reply, parse_message
from wechatpy.exceptions import (InvalidAppIdException,
                                 InvalidSignatureException)
from wechatpy.utils import check_signature


TOKEN = os.getenv("WECHAT_TOKEN", "123456")
EncodingAESKey = os.getenv("WECHAT_ENCODING_AES_KEY", "")
AppId = os.getenv("WECHAT_APP_ID", "")

app = Flask(__name__)


@app.route("/")
def home():
    abort(403)


@app.route("/wechat_reply", methods=["GET", "POST"])
def wechat_reply():
    signature = request.args.get("signature", "")
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    echo_str = request.args.get("echostr", "")
    encrypt_type = request.args.get("encrypt_type", "")
    msg_signature = request.args.get("msg_signature", "")
    try:
        msg = check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)
    msg = parse_message(msg)
    if msg.type == "text":
        reply = create_reply(msg.content, msg)
    else:
        reply = create_reply("Sorry, can not handle this for now", msg)
    return crypto.encrypt_message(reply.render(), nonce, timestamp)
