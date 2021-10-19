import time

from flask import render_template, Flask, request, json, abort, flash, session
# from flask_cors import cross_origin
from jinja2 import select_autoescape, Environment
# from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'Afaccrocazz'
# jinja2 autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))

client = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                     "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
db = client.Users
collection = db.UsersInfo


# Main page
@app.route("/")
def home():
    if 'email' in session:
        return 'You are logged in as ' + session['email']
    return render_template('Main.html')


@app.route("/signup/", methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        _name = request.form['inputName']
        _surname = request.form['inputSurname']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        post = {
            "name": _name,
            "surname": _surname,
            "email": _email,
            "password": _password
        }
        # risolto, togliendo le parentesi quadrate da 'POST' e' andato .-.
        if db.UsersInfo.find_one(post):
            msg = 'Your credential already exist, try again'
            flash(msg)
        else:
            post_info = collection.insert_one(post)
            post_info
            return render_template('Login.html')
    return render_template('Sign_Up.html')


# min 32 vedi il post per il login


# @app.route("/logged in")
# def logged_in():
#     if "user" in session:
#       user =
#        return


@app.route("/signin/", methods=['POST', 'GET'])
def login():
    # if request.method == 'POST':
    #   _email = request.form['inputEmail']
    #  _password = request.form['inputPassword']
    # existing_user = collection.find_one({'email' : _email})
    # if existing_user is None:
    return render_template('Login.html')


@app.route("/logout/")
def logout():
    return render_template('Main.html')


# test page
@app.route("/test/")
def test():
    return render_template('Testing.html')


# user page
@app.route("/user/")
def user():
    return render_template('UserProject.html')


# sw
# @app.route("/sw.js")
# def sw():
#     return app.send_static_file("sw.js")

# Page started in debug modify after, for Pycharm check the IDE launch config
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
