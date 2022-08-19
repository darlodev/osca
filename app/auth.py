##########
# IMPORTS
##########
from flask import Blueprint

##########
# CONFIG
##########
auth = Blueprint("auth", __name__)

##########
# ROUTES
##########
@auth.route("/login")
def login():
    return "Login"

@auth.route("/sgnup")
def signup():
    return "Signup"

@auth.route("/logout")
def logout():
    return "Logout"