from flask import Flask

app = Flask(__name__)


@app.route("/")
def homePage():
    return "<body style=background-color:black;height:100vh><div style=display:flex;justify-content:center;align-items:center><h1 style=color:white;>My first Python Web Page!</h1></div></body>"
