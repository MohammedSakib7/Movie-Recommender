from flask import Flask, render_template
from flask_session import sessions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run()