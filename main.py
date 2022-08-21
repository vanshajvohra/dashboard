from crypt import methods
from unicodedata import name
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route("/")

def hello_world():
    return render_template("index.html")

@app.route("/user/<name>")

def user(name):
    return render_template("user.html", user_name=name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Form Class
class firstname(FlaskForm):
    name = StringField("Enter first name", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create name page
@app.route('/name', methods = ['GET', 'POST'])
def name():
    name = None
    form = firstname
    return render_template("firstname.html")