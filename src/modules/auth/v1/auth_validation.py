from flask import jsonify, request, make_response
from functools import wraps
from src.utils.sendResFormater import sendRes
import re
from marshmallow import Schema,fields,ValidationError, validates,validate

class RegisterSchema(Schema):
    email = fields.Email(
        required=True,
        error_messages={
            'required':'Can not register without email',
            'invalid': 'Invalid email cannot be registered'
        }
    )
    password = fields.Str(
        required=True, 
        validate=fields.Length(min=6),
        error_messages={
            'required':'Password is required',
            'min_length': 'Password must be at least 6 characters long'
        }
    )
    name = fields.Str(
        required=True,
        validate=fields.Length(max=100),
        error_messages={
            'required':'Name is required',
            'max_length': 'Maximum 100 characters allowed'
        }
    )
    address = fields.Str(
        required=True,
        validate=fields.Length(max=100),
        error_messages={
            'required':'address is required',
            'max_length': 'Maximum 100 characters allowed'
        }
    )
    city = fields.Str(
        required=True,
        validate=fields.Length(max=100),
        error_messages={
            'required':'city is required',
            'max_length': 'Maximum 100 characters allowed'
        }
    )
    country = fields.Str(
        required=True,
        validate=fields.Length(max=100),
        error_messages={
            'required':'country is required',
            'max_length': 'Maximum 100 characters allowed'
        }
    )
    phone_number = fields.Str(
        required=True,
        validate=[
            fields.Length(max=20),
            validate.Regexp(regex=r'^\d+$', error="Phone number must contain only numeric characters")
        ],
        error_messages={
            'required':'phone_number is required',
            'max_length': 'Maximum 100 characters allowed'
        }
    )

    # custom validates of password
    @validates('password')
    def validate_password(self, value):
        # Check if password contains at least one uppercase letter
        if not any(char.isupper() for char in value):
            raise ValidationError("Password must contain at least one uppercase letter")

        # Check if password contains at least one lowercase letter
        if not any(char.islower() for char in value):
            raise ValidationError("Password must contain at least one lowercase letter")

        # Check if password contains at least one digit
        if not any(char.isdigit() for char in value):
            raise ValidationError("Password must contain at least one digit")

        # Check if password contains at least one special character
        if not any(char in r'!@#$%^&*()-_=+[{]}\|;:\'",<.>/?`~' for char in value):
            raise ValidationError("Password must contain at least one special character")

        # Check if password is at least 8 characters long
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long")
    
    # custom validation for name field
    @validates('name')
    def validate_name(self,value):
        print(value)
        if value and not value[0].isupper():
            raise ValidationError("First letter of name must be capital")


# define validation middleware
def validate_register_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = request.get_json()

        # intitiate Marshmallow schema
        schema = RegisterSchema()

        try:
            validate_data = schema.load(data)
        except Exception as e:
            error_message = e.messages
            return sendRes(402,message=error_message,isSuccess=False)

        # check if all data are given
        if not data or 'email' not in data or 'password' not in data:
            return sendRes(402, message="Email and password are required", isSuccess=False)

        return fn(*args, **kwargs)
    return wrapper
