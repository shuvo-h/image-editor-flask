# users/v1/routes.py
from flask import Blueprint, jsonify, request


user_bp = Blueprint('users_v1', __name__)



@user_bp.post('/us')
def get_user_v1():
    users = [{"id":1,"username":"Daniel - US"}]
    return jsonify({'users': users})
@user_bp.get('/us')
def get_user_v1y():
    users = [{"id":1,"username":"Daniel - US get"}]
    return jsonify({'users': users})
