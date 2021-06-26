from flask import Flask, session, redirect, render_template, url_for, request
import mimetypes

mimetypes.add_type('application/javascript', '.js')


app = Flask(__name__, template_folder="FLASK/templates", static_folder="FLASK/static")


# Main session page
@app.route("/")
def home():
    return render_template('./Main.html')


@app.route("/test")
def test():
    return render_template('./Testing.html')


# Page started in debug modify after
if __name__ == "__main__":
    app.run(debug=True)
