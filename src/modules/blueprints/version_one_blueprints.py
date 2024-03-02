from .constant_bluprint import VERSIONS
from src.modules import users
from src.modules import auth


# arrange all blueprints for version 1 
blueprint_list = [
    {
        "path": f"/api/{VERSIONS['V1']}/auth",
        "bluePrint": auth.auth_bp_v1
    },
    {
        "path": f"/api/{VERSIONS['V1']}/users",
        "bluePrint": users.users_v1_bp
    },
]
