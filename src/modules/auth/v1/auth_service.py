from flask import jsonify
from src.utils.sendResFormater import sendRes
from src.errorHandlers.appErrorhandler import AppError
from src.modules.users.v1.user_model import User
from . import auth_utils
from src.config.env_config import envs


def registerUserIntoDb(payload):
    email = payload.get('email')
    password = payload.get('password')

    # check if email already exist
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        raise AppError(422, "Email already exist")
    

     # Create a new user instance
    new_user = User(email=email, password=password)
    
    User.add_and_commit(new_user)

    # cookies signin with access_token and refresh_token
    token_payload = {'email': new_user.email, 'user_id': new_user.id}
    access_token = auth_utils.generate_token(token_payload, envs['ACCESS_TOKEN_SECRET'])
    refresh_token = auth_utils.generate_token(token_payload, envs['REFRESH_TOKEN_SECRET'])

    # Create the response
    response = jsonify({
        "data": {
            "user": token_payload,
            "access_token": access_token
        },
        "message": "user registration successful",
        "meta": None,
        "success": True
    })
    response.status_code = 201

     # Set HTTP-only cookies for access token and refresh token
    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=2 * 30 * 24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )


    # return sendRes(202,payload,None,"User registration successfull",True)
    return response



def loginUserFromDb(payload):
    email = payload.get('email')
    password = payload.get('password')

    # check if user exist
    user = User.query.filter_by(email=email).first()
    if not user:
        raise AppError(401,"User not found!")
    

    # match password
    if not User.check_password(user.password,password):
        raise AppError(401,"Password didn't match!")


    # cookies signin with access_token and refresh_token
    token_payload = {'email': user.email, 'user_id': user.id}
    access_token = auth_utils.generate_token(token_payload, envs['ACCESS_TOKEN_SECRET'])
    refresh_token = auth_utils.generate_token(token_payload, envs['REFRESH_TOKEN_SECRET'])

    # Create the response
    response = jsonify({
        "data": {
            "data": {
                "user": token_payload,
                "access_token": access_token
            }
        },
        "message": "User loggedin successful",
        "meta": None,
        "success": True
    })
    response.status_code = 201

     # Set HTTP-only cookies for access token and refresh token
    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=2 * 30 * 24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )


    # return sendRes(202,payload,None,"User registration successfull",True)
    return response