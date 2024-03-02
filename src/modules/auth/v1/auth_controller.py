from flask import jsonify,request
import requests
from src.utils import catchErrorHandler
from src.utils.sendResFormater import sendRes
from . import auth_service



# register a user 
@catchErrorHandler.catch_err_handler
def register_userCtl(body):
    return auth_service.registerUserIntoDb(body)


# login a user 
@catchErrorHandler.catch_err_handler
def login_userCtl(body):
    return auth_service.loginUserFromDb(body)