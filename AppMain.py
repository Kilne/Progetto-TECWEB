from flask import render_template, Flask
from flask_cors import CORS
from jinja2 import select_autoescape, Environment

app = Flask(__name__)
CORS(app)
# jinja2 autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))


# Main page
@app.route("/")
def home():
    return render_template('Main.html')


# test page
@app.route("/test/")
def test():
    return render_template('Testing.html')


# Page started in debug modify after
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
