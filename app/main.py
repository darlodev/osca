##########
# IMPORTS
##########
from flask import Blueprint

##########
# CONFIG
##########
main = Blueprint("main", __name__)

##########
# ROUTES
##########
@main.route("/")
def index():
    return "Index"

@main.route("/profile")
def profile():
    return "profile"