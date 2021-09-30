from flask import render_template, Flask, request, json
from flask_cors import cross_origin
from jinja2 import select_autoescape, Environment
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)
# jinja2 autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))

client = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                     "?retryWrites=true&w=majority")
db = client.Users
collection = db.UsersInfo


# Main page
@app.route("/")
def home():
    return render_template('Main.html')


@app.route("/signup/")
def login():
    return render_template('Sign_Up.html')


@app.route("/signin/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validazione dati
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)
    else:
        return render_template("")
    return render_template('Login.html')


# test page
@app.route("/test/")
def test():
    return render_template('Testing.html')


# user page
@app.route("/user/")
def user():
    return render_template('UserProject.html')


@app.route("/create/")
@cross_origin()
def create():
    ConnectToDB.connect_mongo()
    GettingUserDB.user_db()
    GetUserProjects.get_projects()
    return render_template('CreateProject.html')


# sw
# @app.route("/sw.js")
# def sw():
#     return app.send_static_file("sw.js")


# Page started in debug modify after, for Pycharm check the IDE launch config
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
