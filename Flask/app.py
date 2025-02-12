from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_name(name = None):
    return render_template(
        "website.html",
        name=name,
        date=datetime.now()
   )

