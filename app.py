from flask import Flask
from blueprints.helloworld.helloworld import helloworld_bp
from blueprints.calculator.calculator import calculator_bp

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

# Register the blueprint
# app.register_blueprint(helloworld_bp, url_prefix='/helloworld')
app.register_blueprint(helloworld_bp,)
app.register_blueprint(calculator_bp,url_prefix='/calculator')

if __name__ == '__main__':
    app.run(debug=True)
