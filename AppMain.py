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
# Mongo user collection retrieve route
@app.route("/db/<user>/", methods=["GET"])
@cross_origin()
def obtain_data(user):
    if request.method == "GET":
        # mongo DB connection on server start
        client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                                "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
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
        abort(400)


# Mongo user entry
@app.route("/db/<user>/post", methods=["POST"])
@cross_origin()
def post_data(user):
    if request.method == "POST":
        # mongo DB connection on server start
        client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                                "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
        # Database schema
        user_entry = {}
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
        for K in json_from_fetch:
            user_entry.update({K: json_from_fetch[K]})

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
        abort(400)


# Mongo user single entry collection update
@app.route("/db/<user>/update", methods=["PUT"])
@cross_origin()
def update_entry(user):
    if request.method == "PUT":
        # mongo DB connection on server start
        client_db = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                                "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
        # Database schema
        user_entry = {}
        # connect to user project storage
        user_dbs = client_db.UserProjects
        # User collection container
        user_collection = None

        # If user has a collection to update connect it
        for user_names in user_dbs.list_collection_names():
            if user_names == user:
                user_collection = user_dbs[user_names]
            else:
                client_db.close()
                abort(404)

        # fetch the JSON from request and add it in user entry

        json_from_fetch = request.get_json()
        for K in json_from_fetch:
            user_entry.update({K: json_from_fetch[K]})

        # If fetch went wrong close connection
        if user_entry.get("_id") is None:
            client_db.close()
            return abort(404)
        else:
            # De-sanitize the ID converting to object ID from BSON library
            string_id = user_entry.get("_id")
            user_entry.update({"_id": ObjectId(string_id)})

        # If this is ID is found in document update

        query = {"_id": user_entry["_id"]}
        update_dict = {"$set": {}}

        for K in user_entry:
            if K == "_id":
                continue
            else:
                update_dict["$set"][K] = user_entry[K]

        # Update document combining query and a update dictionary without the object id

        document_to_update = user_collection.find_one_and_update(query, update_dict)
        if document_to_update is not None:
            client_db.close()
            return jsonify({"result": "Update complete"})
        else:
            client_db.close()
            return abort(500)
    else:
        abort(400)


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
