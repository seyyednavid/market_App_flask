from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/about/<username>")
def about_page(username):
    return f"<h1>this is about page of {username}</h1>"