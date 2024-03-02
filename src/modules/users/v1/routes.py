# users/v1/routes.py
from flask import Blueprint, jsonify


users_v1_bp = Blueprint('users_v1', __name__)

@users_v1_bp.route('/')
def get_users_v1():
    users = [{"id":1,"username":"Daniel"}]
    return jsonify({'users': users})
