from flask import Blueprint, render_template, redirect

helloworld_bp = Blueprint("helloworld", __name__, template_folder="templates")

@helloworld_bp.route("/h")
def index():
    return "Hello world"

@helloworld_bp.route("/hello")
def hello():
    return "Hello world again!"

@helloworld_bp.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"

@helloworld_bp.route("/hellohtml")
def hellohtml():
    return render_template('helloworld/hello.html')

