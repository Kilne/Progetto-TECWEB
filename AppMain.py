import flask
from flask import render_template
from flask_pymongo import *

app = flask.Flask(__name__)

# connecting DB
app.config['MONGO_URI'] = "mongodb://127.0.0.1:5000/app_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db


# Main session page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('Main.html')


# test page
@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template('Testing.html')


# db test
@app.route("/add", methods=["GET"])
def add():
    db.tools.insert_one({'title: this is a test', 'body: the body of the test'})
    return flask.jsonify(message="success")


# @TODO:testare il database
@app.route("/show")
def show():
    result = db.tools.find()
    return flask.jsonify([tool for tool in result])


# Page started in debug modify after
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
