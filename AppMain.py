from bson import ObjectId
from flask import render_template, Flask, request, flash, session, redirect, url_for, abort, jsonify
from flask_cors import cross_origin
from jinja2 import select_autoescape, Environment
from pymongo import MongoClient, errors

# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_server_errors
# Flask initialization
app = Flask(__name__)
app.config.from_pyfile('flaskConfig.py')

# jinja2 autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))

client = MongoClient(app.config["DATABASE_URI"], ssl=True, ssl_cert_reqs='CERT_NONE')


# Main page
@app.route("/")
def home():
    if 'username' in session:
        return render_template('Main.html'), flash('You are logged in as ' + session['username'], 'info')
    else:
        return render_template('Main.html'), flash('You are not logged in', 'danger')


@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        db = client.Users
        collection = db.UsersInfo
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
                return redirect(url_for('login'))
        else:
            flash('All fields are required', 'danger')
    return render_template('Sign_Up.html')


@app.route("/signin/", methods=['POST', 'GET'])
def login():
    db = client.Users
    collection = db.UsersInfo
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
            flash('Insert all form fields please', 'info')
    return render_template('Login.html')


@app.route("/logout/")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


# test page
@app.route("/test/")
def test():
    return render_template('Testing.html')


# Create project page
@app.route("/create/")
def create():
    return render_template('CreateProject.html')


# Submitted data route
@app.route("/finalize/", methods=["POST"])
@cross_origin()
def finalize():
    if request.method == "POST":
        # @TODO: get_json non funziona più qui stranamnete ma nel caso passare ai
        #   form.get
        data = request.get_data()
        print(data)
        print("Data end")
        return "200"
    else:
        abort(500)


# user page
@app.route("/user/")
def user():
    if session.get("username") is not None:
        return render_template('UserProject.html')
    else:
        return redirect("/signin/")


# Mongo user collection validation
def validate_user():
    db = client.UserProjects
    try:
        db.validate_collection(session.get("username"))
        return db
    except errors.OperationFailure:
        return False


# Mongo user data collection getter
@app.route("/db/getALL/", methods=["GET", "POST"])
@cross_origin()
def get_documents():
    if request.method == "GET" or request.method == "POST":
        db = validate_user()

        if not db:
            abort(404)

        user_storage = db[session.get("username")]

        query_result = []

        if user_storage.count_documents({}) == 0:
            return jsonify({"result": None})
        else:
            for document in user_storage.find():
                temp_dict = document
                temp_dict["_id"] = str(temp_dict["_id"])
                query_result.append(temp_dict)

        return jsonify(query_result)
    else:
        abort(403)


# Mongo user single document upload
@app.route("/db/addONE/", methods=["POST"])
@cross_origin()
def add_document():
    if request.method == "POST":
        db = validate_user()

        if not db:
            abort(404)

        user_storage = db[session.get("username")]

        dict_for_mongo = request.get_json()

        if dict_for_mongo is None:
            abort(500)

        if user_storage.insert_one(dict_for_mongo).acknowledged:
            return jsonify({"result": True})
        else:
            abort(500)
    else:
        abort(402)


# Mongo update document by id
@app.route("/db/updateONE/", methods=["PUT"])
@cross_origin()
def update():
    if request.method == "PUT":
        db = validate_user()

        if not db:
            abort(404)

        coll = db[session.get("username")]

        dict_for_update = request.get_json()

        dict_for_update["_id"] = ObjectId(dict_for_update["_id"])

        pop_id = ""

        try:
            pop_id = dict_for_update.pop("_id")
        except KeyError:
            abort(500)

        try:
            coll.find_one_and_update({"_id": pop_id}, {"$set": dict_for_update})
            return jsonify({"result": True})
        except errors.PyMongoError:
            abort(500)
    else:
        abort(402)


# Mongo delete single document by id
@app.route("/db/deleteONE/", methods=["DELETE"])
@cross_origin()
def delete_one():
    if request.method == "DELETE":
        db = validate_user()

        if not db:
            abort(404)

        coll = db[session.get("username")]

        value_to_delete = request.get_json()

        value_to_delete["_id"] = ObjectId(value_to_delete["_id"])

        if coll.find_one_and_delete(value_to_delete) is not None:
            return jsonify({"result": True})
        else:
            abort(500)
    else:
        abort(402)


# sw
# @app.route("/sw.js")
# def sw():
#     return app.send_static_file("sw.js")

# Page started in debug modify after, for Pycharm check the IDE launch config
if __name__ == "__main__":
    app.run("127.0.0.1", 5000)
