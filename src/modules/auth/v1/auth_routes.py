from flask import Blueprint, jsonify, request, make_response
import random, datetime
import jwt  # Import PyJWT library
from . import auth_utils
from src.config.env_config import envs
from src.config.db_config import db
from src.modules.users.v1.user_model import User

auth_bp_v1 = Blueprint("auth_v1",__name__)

# Simulated user database
users = [
    {"email": "user1@example.com", "password": "password1"},
    {"email": "user2@example.com", "password": "password2"}
]


# login a user
@auth_bp_v1.post("/login")
def loginRoute():
    bodyData = request.json
    print(bodyData)

    if not bodyData:
        return jsonify({"msg":"body is required",}), 400
    
    if not bodyData.get('email') or not bodyData.get('password'):
        return jsonify({"msg":"email and password is required",}), 400
    
    for existUser in users:
        if (existUser['email'] == bodyData.get('email')) and  (existUser['password'] == bodyData.get('password')):
            access_token = auth_utils.generate_token({'email': existUser["email"]}, envs['ACCESS_TOKEN_SECRET'])
            refresh_token = auth_utils.generate_token({'email': existUser["email"]}, envs['REFRESH_TOKEN_SECRET'])
            

             # Create the response
            response = jsonify({"msg": "Login successful","access_token":access_token})
            response.status_code = 200

            # Set HTTP-only cookies for access token and refresh token
            response.set_cookie(
                key="access_token", 
                value=access_token, 
                max_age= 24 * 60 * 60,
                path="/", 
                secure=True, 
                httponly=True
            )
            response.set_cookie(
                key="refresh_token", 
                value=refresh_token, 
                max_age= 2 *30 * 24 * 60 * 60,
                path="/", 
                secure=True, 
                httponly=True
            )

            return response
            
    return jsonify({"msg":"Incorrect email and password",}), 401



@auth_bp_v1.get("/me")
def getMe():
    # Retrieve access token from cookies
    access_token = request.cookies.get('access_token')

    if not access_token:
        return jsonify({"msg": "Access token missing"}), 401
    
    # Verify access token
    token_payload = auth_utils.verify_jwt_token(access_token,envs['ACCESS_TOKEN_SECRET'])

    if token_payload is None:
        return jsonify({"msg": "Invalid or expired access token"}), 401
    
    
    return jsonify({"msg":"Me info successful", **token_payload,}), 200


# insert a user 
@auth_bp_v1.post("/add")
def insertUser():
    bodyData = request.json
    password = bodyData.get('password')
    email = bodyData.get('email')
    new_user = User(password=password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg":"User added successful",}), 200