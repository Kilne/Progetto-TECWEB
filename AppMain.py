from flask import render_template, Flask
from flask_cors import CORS
from jinja2 import select_autoescape, Environment
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
# jinja2 autoescape
env = Environment(autoescape=select_autoescape(
    enabled_extensions=('html', 'xml'),
    default_for_string=True,
))

# connessione funziona anche se senza SSL , capire perchè stampa due volte l'ID
# MongoDB atlas connection client
clientDB = MongoClient("mongodb+srv://Luca:WliL3VbEqdbl5VAX@clusterprogetto.0ocor.mongodb.net/ClusterProgetto"
                       "?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs='CERT_NONE')
# @TODO: VEDERE PERCHè STAMPA DUE VOLTE
# dbObject = clientDB.ClusterProgetto
# collectionTest = dbObject.CollTest
# post = {
#     "author": "Luca",
#     "test": "yes"
# }
# id_inserted = collectionTest.insert_one(post).inserted_id
# print(id_inserted)


# Main page
@app.route("/")
def home():
    return render_template('Main.html')


# test page
@app.route("/test/")
def test():
    return render_template('Testing.html')


# Page started in debug modify after
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
