from flask import render_template, Flask, jsonify
from flask_cors import cross_origin
from jinja2 import select_autoescape, Environment
from MONGOUTILS.FindUserData import find_data

app = Flask(__name__)
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
@cross_origin()
def test():
    print(find_data("UserTest"))
    return render_template('Testing.html')


@app.route("/test/db")
@cross_origin()
def get_data():
    return jsonify(find_data("User2Test"))


# user page
@app.route("/user/")
def user():
    return render_template('UserProject.html')


@app.route("/create/")
@cross_origin()
def create():
    return render_template('CreateProject.html')


# sw
# @app.route("/sw.js")
# def sw():
#     return app.send_static_file("sw.js")


# Page started in debug modify after, for Pycharm check the IDE launch config
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
