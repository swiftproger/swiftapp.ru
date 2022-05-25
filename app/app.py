from flask import Flask, Response

application = Flask(__name__)

@application.route("/")
def index():
    return "swiftapp"


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port="80", debug=True)
    application.run(debug=False)
