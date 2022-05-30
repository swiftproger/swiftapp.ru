from flask import Flask

app = Flask(__name__)


@app.route("/start")
def hello():
   return "<h1 style='color:blue'>Hello!</h1>"


@app.route('/', subdomain='<subdomain>')
def handler(subdomain):
   return f"{subdomain}.swiftapp.ru!"


if __name__ == "__main__":
   app.run(host='0.0.0.0')
