from flask import render_template, Flask

app = Flask(__name__)


# Main session page
@app.route("/")
def home():
    return render_template('Main.html')


@app.route("/sw.js", methods=["GET"])
def sw():
    return app.send_static_file('sw.js')


# test page
@app.route("/test/")
def test():
    return render_template('Testing.html')


# Page started in debug modify after
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
