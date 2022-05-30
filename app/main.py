from flask import Flask

app = Flask(__name__, subdomain_matching=True)

app.config['SERVER_NAME'] = 'swiftapp.ru'
app.url_map.default_subdomain = "www"

#
# @app.route("/")
# def hello():
#    return "<h1 style='color:blue'>Hello!!!</h1>"


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


# @app.route('/', subdomain='<string:subdomain>', methods=['GET', 'POST'])
# def handler(subdomain):

   # return f"{subdomain}.swiftapp.ru!!"


if __name__ == "__main__":
   app.run(host='0.0.0.0')
