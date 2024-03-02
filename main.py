from dotenv import load_dotenv
from src.app_operator import app_controller

# Load all env variables from .env file 
load_dotenv()

combined_app = app_controller.create_combined_app()

if __name__ == '__main__':
    # run only one app at a time 
    combined_app.run()