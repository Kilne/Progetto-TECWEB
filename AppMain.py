from flask import Flask, render_template, url_for

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
    app.run(debug=True)
