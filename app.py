from flask import Flask, redirect, render_template, url_for, request, session, flask 
from flask_session import sessions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    render_template(login.html)


if __name__ == "__main__":
    app.run()