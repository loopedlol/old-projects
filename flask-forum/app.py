from flask import Flask, render_template

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/general')
def general():
  return render_template("general.html")

@app.route('/games')
def games():
  return render_template("games.html")

@app.route('/books')
def books():
  return render_template("books.html")

@app.route('/tv')
def tv():
  return render_template("tv.html")

@app.route('/about')
def about():
  return render_template("about.html")

if __name__ == '__main__':
  import os
  HOST = os.environ.get("SERVER_HOST", "localhost")
  try:
    PORT = int(os.environ.get("SERVER_PORT", "5555"))
  except ValueError:
    PORT = 5555
  app.run(HOST, PORT)
