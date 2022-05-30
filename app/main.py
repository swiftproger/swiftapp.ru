from flask import Flask

app = Flask(__name__, subdomain_matching=True)
# app = Flask(__name__)

app.config['SERVER_NAME'] = '*.swiftapp.ru'
app.url_map.default_subdomain = "www"


@app.route("/")
def index():
    return "example.com 15"

@app.route("/user/<int:id>")
def user(id):
    return f"{id}.example.com"


@app.route("/d", subdomain="api")
def egg_index():
    return "api.example.com"




if __name__ == "__main__":
   app.run(host='0.0.0.0')
