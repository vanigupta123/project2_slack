import os
import json

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime

channels_list = list()
msg = dict()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/channels", methods=["POST"])
def channels():
    channel = request.form.get("chan")
    msg[channel] = []
    if channel not in channels_list:
        channels_list.append(channel)
        return jsonify({"error":False, "new_channel":channel})
    else:
        return jsonify({"error":True})

@app.route("/populate_channels")
def populate_channels():
    return jsonify({"chans":json.dumps(channels_list)})

@app.route("/<string:channel_name>.html")
def in_channel(channel_name):
    print("I am sending you to a channel")
    msgs = msg[channel_name]
    return render_template("channel.html", msgs=msgs, channel_name=channel_name)

@socketio.on("submit message")
def message(data):
    print("at submit message")
    username = data["username"]
    message = data["message"]
    timestamp = datetime.now()
    channel = data["channel"]
    ts = str(timestamp)
    msg[channel].append([username, message, timestamp])
    if len(msg[channel]) == 101:
        msg[channel].pop(0)
    print(msg)
    emit('announce message', {'channel': channel, 'username': username, 'message': message, 'timestamp': ts}, broadcast=True)


