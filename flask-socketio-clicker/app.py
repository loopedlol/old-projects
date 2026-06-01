from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Received message: {msg}")
    send(f"Echo: {msg}")

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 5000
    socketio.run(app, debug=True)