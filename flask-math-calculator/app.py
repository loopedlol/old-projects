from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/factorial/<int:n>")
def factorial(n):
  fact = 1
  for i in range(1, n + 1):
    fact = fact * i
  return f"{fact}"

@app.route("/fibonacci/<int:n>")
def fibonacci(n):
  a = 0
  b = 1
  output = 0
  if n < 0:
    print("ERROR")
  elif n == 0:
    output = a
  elif n == 1:
    output = b
  else:
    for i in range(2, n):
      c = a + b
      a = b
      b = c
    output = b
  return f"{output}"

@app.route("/average/<int:a>/<int:b>")
def average(a, b):
  return f"{(a + b) / 2}"

if __name__ == '__main__':
  app.run()
