from flask import render_template, Flask
from pymongo import MongoClient

app = Flask(__name__)

# connecting DB
app.config['MONGO_URI'] = "mongodb://127.0.0.1:5000/app_db"
mongodb_client = MongoClient(app)
db = mongodb_client.db


# Main session page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('Main.html')


# test page
@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template('Testing.html')


# Page started in debug modify after
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
