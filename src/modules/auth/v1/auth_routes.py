from flask import Blueprint, jsonify, request, make_response
import random, datetime
import jwt  # Import PyJWT library

auth_bp_v1 = Blueprint("auth_v1",__name__)

# Simulated user database
users = [
    {"email": "user1@example.com", "password": "password1"},
    {"email": "user2@example.com", "password": "password2"}
]

# Generate tokens (For demo purposes)
def generate_tokens(email):
    access_token_payload = {"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}  # Set expiration time for 1 hour
    access_token = jwt.encode(access_token_payload, 'secret_key', algorithm='HS256')

    refresh_token_payload = {"email": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)}  # Set expiration time for 7 days
    refresh_token = jwt.encode(refresh_token_payload, 'secret_key', algorithm='HS256')
    
    return access_token, refresh_token

# Verify JWT token
def verify_token(token):
    try:
        # Decode the token using the secret key
        payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        return None

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
            access_token, refresh_token = generate_tokens(existUser["email"])
            # print(access_token)

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
    token_payload = verify_token(access_token)

    if token_payload is None:
        return jsonify({"msg": "Invalid or expired access token"}), 401
    
    
    return jsonify({"msg":"Me info successful", **token_payload,}), 200