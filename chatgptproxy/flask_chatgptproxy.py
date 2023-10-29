import os

import openai
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource
from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/")
def home():
    abort(403)

@app.route("/openai/chat_completion/create", methods=["POST"])
def openai_chat_completion_create():
    data = request.get_json()
    response: EngineAPIResource = openai.ChatCompletion.create(**data)
    return response
