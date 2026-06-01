from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-session-key")

wsgi_app = app.wsgi_app

@app.route('/')
def index():
  if "username" in session:
    return render_template("welcome.html", username=session["username"])
  else:
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
  if request.method == "POST":
    session["username"] = request.form["username"]
    return render_template("welcome.html", username=session["username"])
  else:
    return render_template("login.html")

@app.route("/logout")
def logout():
  session.pop("username", None)
  return render_template("index.html")

if __name__ == '__main__':
  HOST = os.environ.get("SERVER_HOST", "localhost")
  try:
    PORT = int(os.environ.get("SERVER_PORT", "5555"))
  except ValueError:
    PORT = 5555
  app.run(HOST, PORT)
