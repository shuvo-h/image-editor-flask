from flask import jsonify, request, make_response
from functools import wraps
from src.utils.sendResFormater import sendRes
import re

def validate_register_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = request.get_json()

        # check if all data are given
        if not data or 'email' not in data or 'password' not in data:
            return sendRes(402, message="Email and password are required", isSuccess=False)
        
         # Check if the email is valid
        email = data.get('email', '')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return sendRes(402, message="Invalid email format", isSuccess=False)

        # Check if the password contains at least 6 characters
        password = data.get('password', '')
        if len(password) < 6:
            return sendRes(402, message="Password must be at least 6 characters long", isSuccess=False)

        return fn(*args, **kwargs)
    return wrapper
