from flask import render_template, Flask, request, json, abort, flash, session, redirect, url_for
from datetime import timedelta
# from flask_cors import cross_origin
from jinja2 import select_autoescape, Environment
# from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'A_facc_ro_cazz'
app.permanent_session_lifetime = timedelta(hours=1)
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
    if 'username' in session:
        return render_template('Main.html'), flash('You are logged in as ' + session['username'], 'info')
    else:
        return render_template('Main.html'), flash('You are not logged in', 'danger')


@app.route("/signup/", methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        _name = request.form['inputName']
        _surname = request.form['inputSurname']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # risolto, togliendo le parentesi quadrate da 'POST' e' andato .-.
        if _name and _surname and _email and _password:
            if db.UsersInfo.find_one({'email': _email}):
                flash('Your credential already exist, try again', 'danger')
            else:
                info = {
                    "name": _name,
                    "surname": _surname,
                    "email": _email,
                    "password": _password
                }
                save_info = collection.insert_one(info)
                save_info
                return redirect(url_for('login'))
        else:
            flash('Insert all the camps', 'danger')
    return render_template('Sign_Up.html')


@app.route("/signin/", methods=['POST', 'GET'])
def login():
    if 'username' in session:
        flash('You are already logged in!', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        existing_user = collection.find_one({"name": _name, "email": _email, "password": _password})
        if existing_user is None:
            flash('Your credential are wrong, try again', 'danger')
        elif _name and _email and _password:
            session.permanent = True
            _username = _name
            session['username'] = _name
            return redirect(url_for('home'))
        else:
            flash('Insert all camps please', 'info')
    return render_template('Login.html')


@app.route("/logout/")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


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
