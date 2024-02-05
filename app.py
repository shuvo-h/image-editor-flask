from flask import Flask
from blueprints.helloworld.helloworld import helloworld_bp
from blueprints.calculator.calculator import calculator_bp
from blueprints.users.users import users_bp

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

# Register the blueprint
# app.register_blueprint(helloworld_bp, url_prefix='/helloworld')
app.register_blueprint(helloworld_bp,)
app.register_blueprint(calculator_bp,url_prefix='/calculator')
app.register_blueprint(users_bp, url_prefix='/api/v1/users')

if __name__ == '__main__':
    app.run(debug=True)
