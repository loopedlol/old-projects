from flask import Flask, render_template#, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", myList = [1, 2, 3])

@app.route('/1')
def doorOne():
  return render_template("prize.html")

@app.route('/2')
def doorTwo():
  return render_template("goat.html")

@app.route('/3')
def doorThree():
  return render_template("goat.html")

if __name__ == '__main__':
  app.run()