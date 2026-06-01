from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-auth-db-key")

@app.route('/')
def index():
  return render_template("home.html")

if __name__ == '__main__':
  app.run()
