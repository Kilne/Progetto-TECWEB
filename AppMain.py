from flask import render_template, Flask
from flask_cors import CORS
from jinja2 import select_autoescape, Environment
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
# jinja2 autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))


# connessione funziona anche se senza SSL , capire perchè stampa due volte l'ID
# MongoDB atlas connection client
# clientDB = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
#                        "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')


# Main page
@app.route("/")
def home():
    return render_template('Main.html')


# test page
@app.route("/test/")
def test():
    return render_template('Testing.html')


# user page
@app.route("/user/")
def user():
    return render_template('UserProject.html')


@app.route("/create/")
def create():
    return render_template('CreateProject.html')


# sw
# @app.route("/sw.js")
# def sw():
#     return app.send_static_file("sw.js")


# Page started in debug modify after, for Pycharm check the IDE launch config
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
