from flask import Blueprint, render_template, redirect,url_for

calculator_bp = Blueprint('calculator',__name__,template_folder='templates')

@calculator_bp.route("/")
def index():
    return "THis is calculator blueprint"

@calculator_bp.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    return str(num1 + num2)

@calculator_bp.route("/substract/<int:num1>/<int:num2>")
def substract(num1,num2):
    return str(num1 - num2)

@calculator_bp.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1,num2):
    return str(num1 * num2)

@calculator_bp.route("/devide/<int:num1>/<int:num2>")
def devide(num1,num2):
    return str(num1 / num2)

# we are telling the calculator route to redirect helloworld app route
@calculator_bp.route("/go_to_hello")
def go_to_hello():
    return redirect(url_for("helloworld.hellohtml"))