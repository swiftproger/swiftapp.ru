from flask import Flask

app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = "swiftapp.ru:80"


@app.route('/')
def index():
    return "swiftapp.ru"


@app.route("/", subdomain="api")
def egg_index():
    return "api.swiftapp.ru"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)
