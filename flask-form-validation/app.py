from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods = ["POST", "GET"])
def login():
  message = ""
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    demo_username = os.environ.get("DEMO_USERNAME", "demo")
    demo_password = os.environ.get("DEMO_PASSWORD", "password")
    if username == demo_username and password == demo_password:
      message = "login successful"
      return render_template("welcome.html", message = message)
    else:
      message = "wrong username and password"
  return render_template("index.html", message = message)

if __name__ == '__main__':
  app.run()
