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


# Mongo user collection retrieve route
@app.route("/db/<string:user>/", methods=["GET"])
@cross_origin()
def obtain_data(user):
    # mongo DB connection on server start
    client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                            "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
    if request.method == "GET":
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
                client_db.close()
                abort(404)
        # prepare sanitized data container
        sanitized_id_data = []
        # cycle trough documents and sanitize the "_id" type
        for document in user_collection.find():
            document["_id"] = str(document["_id"])
            sanitized_id_data.append(document)
        # return the data in JSON format and close the DB
        client_db.close()
        return jsonify(sanitized_id_data)
    else:
        client_db.close()
        abort(404)


# Mongo user entry
@app.route("/db/<string:user>/post", methods=["POST"])
@cross_origin()
def post_data(user):
    # mongo DB connection on server start
    client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                            "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
    # Database schema @TODO:farti dare lo schema dal server e poi controllare che sia uguale?
    user_entry = {
        "owner": "",
        "project_number": 0,
        "objective": "",
        "percentage": 0.0,
        "proj_name": ""
    }

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
                client_db.close()
                abort(404)
        # Cycle trough @user_entry and at the same time use the dict keys to cycle in the HTTP flask object @request
        # stored in the @json_from_fetch for simple handling the keys
        # references: https://pythonise.com/series/learning-flask/working-with-json-in-flask
        # https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
        # https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request
        json_from_fetch = request.get_json()
        for K in user_entry:
            user_entry[K] = json_from_fetch[K]
        # Pymongo tries to insert the post if it succeeds it returns a acknowledged response bool in JSON format
        # if it fails it closes the DB and return a INTERNAL SERVER ERROR PAGE
        # reference: https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult
        insertion_result = user_collection.insert_one(user_entry).acknowledged
        if insertion_result:
            client_db.close()
            return jsonify({"result": insertion_result})
        else:
            client_db.close()
            abort(500)
    else:
        client_db.close()
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
