from flask import jsonify,request
from .users import users_bp
from .userController import get_all_users_controller

@users_bp.route("/all-users")
def all_users_route():
    query_params = request.args.to_dict()
    users = get_all_users_controller(query_params)
    return jsonify(users)
