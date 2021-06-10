from flask import Flask, session, redirect, render_template, url_for, request

app = Flask(__name__)


# Main session page
@app.route("/")
def home():
    return render_template('WEB FILES/HTML/Main.html')


# Page started in debug modify after
if __name__ == "__main__":
    app.run(debug=True)
