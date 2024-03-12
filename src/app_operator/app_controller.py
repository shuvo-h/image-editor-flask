from flask import Flask, jsonify
from src.blueprints import bp_manager
from src.config import db_config
from src.utils.sendResFormater import sendRes
from src.errorHandlers.appErrorhandler import AppError
from src.errorHandlers import databaseErrorHandler

def create_combined_app():
    app = Flask(__name__)

    # configure app to add all secret from env
    # Call middleware configuration functions
    # configure_cors(app)
    # configure_logging(app)
    # configure_csrf(app)
    # configure_xss(app)
    # configure_secure_cookies(app)
    # configure_request_rate_limiting(app)
    # configure_csp(app)

    # connect DB
    db_config.connectDb(app)

    # register all blueprints
    bp_manager.register_blueprints(app)

    # handle custom error page
    # handle invalid url
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'success':False,"message":"URL not found 😞"}),404
    # Internal server error handler 
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({'success':False,"message":"Internal server error 😞"}),500
    
    # Exception error handler
    @app.errorhandler(Exception)
    def handle_exception(error):
        # any custom error raise/throw will received here
        errMessage = databaseErrorHandler.format_error_message(error) or "Internal server error 😞"
        response = jsonify({'error': str(error)})
        status_code = error.status_code if hasattr(error,'status_code') else 500
        return sendRes(status_code,None,None,errMessage,False)
    
    @app.errorhandler(AppError)
    def handle_app_error(error):
        response = sendRes(error.status_code, message=str(error), isSuccess=False)
        return response

    
    # Configure versioning
    # configure_versioning(app)

    # Configure cache
    # configure_cache(app)

    # Configure background tasks
    # configure_background_tasks(app)


    return app