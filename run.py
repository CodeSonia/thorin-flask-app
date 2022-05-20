import os
import json 
# Imports flask
# The capital "F" indicates it is a class
# import render_template from flask
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


# Create an instance of Flask and store it in var app:
# The first arg __name__ is the name of the package.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# Use a @ decorator to wrap functions
# All func are obj, and obj can be passed around
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data: 
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")
  

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    # Run the app with the below arguments
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
