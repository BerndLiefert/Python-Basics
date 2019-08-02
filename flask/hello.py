from flask import Flask
app = Flask(__name__)

#https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application

@app.route("/")
def hello():
    return "Hello World!"
