from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-session-key")

@app.route('/')
def index():
  session["visits"] = session.get("visits", 0) + 1
  return render_template("welcome.html", username=session.get("username", ""), count=session["visits"])

@app.route('/login', methods = ['GET', 'POST'])
def login():
  if request.method == "POST":
    session["username"] = request.form["username"]
    session["visits"] = session.get("visits", 0) + 1
    return render_template("welcome.html", username=session["username"], count=session["visits"])
  else:
    return render_template("login.html")

@app.route('/logout')
def logout():
  session.pop("username", None)
  return render_template("index.html")

if __name__ == '__main__':
  app.run()
