from flask import Flask, render_template

app = Flask(__name__)


# Main session page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('Main.html')


@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template('Testing.html')


# Page started in debug modify after
if __name__ == "__main__":
    app.run('127.0.0.1', debug=True, port=5000, ssl_context='adhoc')
