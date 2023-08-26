import os
import urllib
import requests
from flask import redirect, render_template, request, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(movie):
    """Look up quote for symbol."""

    for char in movie:
        apientry = movie.strip().replace(" ", "+")
    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={urllib.parse.quote_plus(movie)}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    try:
        srch = response.json() 
        # results = {
        #     "title": srch["Title"],
        #     "year": srch["year"],
        #     "symbol": srch["symbol"],
        #     "imdbID": srch["imdbID"],
        #     "type" : srch["Type"],
        # }
        # if srch["poster"]:
        #     results["poster"] = srch["poster"]
        
        return srch['Search']
    except (KeyError, TypeError, ValueError):
        return None


