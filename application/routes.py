from application import app
from flask import render_template
# from application.models import User, Course, Enrollment

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/about")
def about():
    return render_template("index.html", about = True)

@app.route("/work")
def work():
    return render_template("index.html", work = True)

@app.route("/blog")
def blog():
    return render_template("index.html", blog = True)
