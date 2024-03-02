from flask_sqlalchemy import SQLAlchemy
from .env_config import envs

# intitiate database 
db = SQLAlchemy()

# configure database
def connectDb(app):
    # Configure the database URI   'mysql://username:password@localhost/db_name'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{envs['DB_USERNAME']}:{envs['DB_PASSWORD']}@{envs['DB_HOST']}/{envs['DB_NAME']}"


    # Suppress deprecation warnings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the Flask application
    db.init_app(app)

     # Create all database tables
    with app.app_context():
        db.create_all()