from src.modules.blueprints.constant_bluprint import VERSIONS
from src.modules import users


# arrange all blueprints for version 1 
blueprint_list = [
    {
        "path": f"/api/{VERSIONS['V1']}/users",
        "bluePrint": users.users_v1_bp
    },
]
