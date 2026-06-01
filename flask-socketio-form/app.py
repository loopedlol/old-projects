from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "dev-socket-key")

socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template("index.html")

@socketio.on("form_submitted", namespace="/test")
def get_message_from_form(msg):
  emit("a_new_message", {"data": msg["data"]})

if __name__ == '__main__':
  socketio.run(app)
