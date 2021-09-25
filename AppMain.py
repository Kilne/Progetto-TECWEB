from flask import render_template, Flask, jsonify, abort, request
from flask_cors import cross_origin
from jinja2 import select_autoescape, Environment
from pymongo import MongoClient

# the main name of the flask app
app = Flask(__name__)
# jinja2 autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))
# mongo DB connection on server start
client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                        "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')


# Main page
@app.route("/")
def home():
    return render_template('Main.html')


# test page
@app.route("/test/")
@cross_origin()
def test():
    return render_template('Testing.html')


# Mongo user collection retrieve route
@app.route("/db/<string:user>", methods=["POST"])
@cross_origin()
def get_data(user):
    if request.method == "POST":
        # connect to user project storage
        user_dbs = client_db.UserProjects
        # initialize user collection container
        user_collection = None
        # cycle trough the collections searching for the user one, if not present 404
        for collection_of_user in user_dbs.list_collection_names():
            if collection_of_user == user:
                # if found store the collection
                user_collection = user_dbs[collection_of_user]
            else:
                abort(404)
        # prepare sanitized data container
        sanitized_id_data = []
        # cycle trough documents and sanitize the "_id" type
        for document in user_collection.find():
            document["_id"] = str(document["_id"])
            sanitized_id_data.append(document)
        # return the data in JSON format
        data = {"data": sanitized_id_data}
        return jsonify(data)
    else:
        abort(404)


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
