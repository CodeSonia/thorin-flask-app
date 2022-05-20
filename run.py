import os
# Imports flask
# The capital "F" indicates it is a class
# import render_template from flask
from flask import Flask, render_template


# Create an instance of Flask and store it in var app:
# The first arg __name__ is the name of the package.
app = Flask(__name__)


# Use a @ decorator to wrap functions
# All func are obj, and obj can be passed around
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # Run the app with the below arguments
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
