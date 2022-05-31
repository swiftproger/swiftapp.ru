from flask import Flask
from flask import Blueprint

app = Flask(__name__)
app.config['SERVER_NAME'] = 'swiftapp.ru'

@app.route('/')
def hello_world():
    return 'Hello World!'

# Blueprint declaration
bp = Blueprint('subdomain', __name__, subdomain="<user>")

# Add a route to the blueprint
@bp.route("/")
def home(user):
    return 'Welcome to your subdomain, {}'.format(user)

# Register the blueprint into the application
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)