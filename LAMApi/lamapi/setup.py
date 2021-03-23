from flask import Flask, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

def setupFlaskApplication():
    app = Flask(__name__)
    app.config.from_object('lamapi.config.LAMConfiguration')
    config = app.config
    return app

def setupFlaskExtensions(app):
    api = Api(app)
    db = SQLAlchemy(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    jwt = JWTManager(app)
    return api, db, cors, jwt

def setupFlaskResources(api):
    from lamapi.config import LAMConfiguration
    from lamapi.auth.controller import AuthController
    from lamapi.music.controller import MusicController
    from lamapi.permission.controller import PermissionController
    from lamapi.type.controller import TypeController

    api.add_resource(MusicController, '/music')
    api.add_resource(AuthController, '/auth')
    api.add_resource(PermissionController, '/permission')
    api.add_resource(TypeController, '/type')