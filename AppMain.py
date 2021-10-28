from bson.objectid import ObjectId
from flask import render_template, Flask, jsonify, abort, request
from flask_cors import cross_origin
from jinja2 import select_autoescape, Environment
from pymongo import MongoClient

# WEB PAGE ERROR CODES GUIDE: https://moz.com/learn/seo/http-status-codes
# the main name of the flask app
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
    return render_template('Testing.html')


# https://www.restapitutorial.com/lessons/httpmethods.html
# references: https://pythonise.com/series/learning-flask/working-with-json-in-flask
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
# https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request
# reference: https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult


# user page
@app.route("/user/")
def user():
    return render_template('UserProject.html')


@app.route("/create/")
@cross_origin()
def create():
    return render_template('CreateProject.html')


# sw DEPRECATED
# @app.route("/sw.js")
# def sw():
#     return app.send_static_file("sw.js")


# Page started in debug modify after, for Pycharm check the IDE launch config
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
