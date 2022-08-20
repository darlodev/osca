##########
# IMPORTS
##########
from flask import Flask
from pymongo import MongoClient
from flask_mongoengine import MongoEngine

##########
# CONFIG
##########
def create_app():
    app = Flask(__name__)

    ##########
    # DATABASE
    ##########
    app.config["MONGODB_SETTING"] = {
        "db": "osca_database",
        "host": "localhost",
        "port": 27017
    }
    db = MongoEngine()
    db.init_app(app)

    class User(db.Document):
        name = db.StringField()
        email = db.StringField()
        password = db.StringField()


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app