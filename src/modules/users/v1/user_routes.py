# users/v1/routes.py
from flask import Blueprint, jsonify


users_v1_bp = Blueprint('users_v1', __name__)

@users_v1_bp.route('/')
def get_users_v1():
    users = [{"id":1,"username":"Daniel"}]
    return jsonify({'users': users})

@users_v1_bp.post('/us')
def get_user_v1():
    users = [{"id":1,"username":"Daniel - US"}]
    return jsonify({'users': users})
@users_v1_bp.get('/us')
def get_user_v1y():
    users = [{"id":1,"username":"Daniel - US get"}]
    return jsonify({'users': users})
