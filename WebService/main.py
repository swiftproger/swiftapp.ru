from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "swiftapp.ru _"


@app.route("/", subdomain="static")
def static_index():
    """Flask supports static subdomains
    This is available at static.your-domain.tld"""
    return "static.your-domain.tld"


@app.route("/dynamic", subdomain="<username>")
def username_index(username):
    """Dynamic subdomains are also supported
    Try going to user1.your-domain.tld/dynamic"""
    return username + ".your-domain.tld"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
