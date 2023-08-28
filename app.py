import sqlite3
from flask import Flask, redirect, render_template, url_for, request, session, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime as d
import os

# Import login decorator from helpers function
from helpers import login_required, lookup

# Initialize flask framework
app = Flask(__name__)

# Use filesystem instead of signed cookies to store session information on server side
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# API key for OMDB movie metadata, Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# API key for Youtube to display trailers for movies on a video player


# Initialized SQL database that stores liked movies on a table along with movie information from OMDB movie database, maybe include my own tables of movie information from IMDB to query easily
# db = sqlite3.connect(...)

# Basic Homepage displaying movie information. If user is signed in, displays a list of recommended movies to watch along side other top movies.
@app.route("/", methods=["GET", "POST"])
def index():
    # if request.method == "POST":
    #     return redirect(url_for("search", Json_result=lookup(request.form.get('search'))))
    # else:
     return render_template("index.html")


# User authentication using login decorator from helpers.py and save user sessions in flask_session as files
@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    This page authenticates users based on their usernames and password hashes through a form
    '''
    if request.method == "POST" :
        # Get username and password from form, if user exits and password hash matches, create a session
        # Render the template for index with favorites page and top recommendations
        user = request.form["username"]
        session["user"] = user
        # Return error if user does not exit or password does not match
        return redirect("/")
    else:
        # Render the login page
        return render_template("login.html")

# This might be removed but this displays a homepage for users who are logged in
@app.route("/favorites")
@login_required
def favorites():
    '''
    This is a page with the bookmarked movies by users
    '''
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return render_template(url_for("login"))

@app.route("/search", methods=["POST"])
def search():
    '''
    Displays a page with search results, takes input from the navbar search form
    '''
    x = lookup(request.form.get("search"))
    if x:
        print(x)
    return render_template("search.html", json_results=x)

if __name__ == "__main__":
    app.run(debug=True)