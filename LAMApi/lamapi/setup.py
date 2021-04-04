from flask import Flask, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager, \
    unset_access_cookies, unset_jwt_cookies

import json

def createApplication(config):
    from lamapi import db

    app = Flask(__name__)
    app.config.from_object(config)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    api = Api(app)
    db.init_app(app)
    cors = CORS(app, 
        resources={r"/*": {"origins": "*"}}, 
        supports_credentials=True
    )
    jwt = JWTManager(app)

    from lamapi.config import LAMConfiguration
    from lamapi.auth.controller import AuthController
    from lamapi.music.controller import MusicController
    from lamapi.permission.controller import PermissionController
    from lamapi.type.controller import TypeController

    api.add_resource(MusicController, '/music')
    api.add_resource(AuthController, '/auth')
    api.add_resource(PermissionController, '/permission')
    api.add_resource(TypeController, '/type')

    @app.before_first_request
    def create_tables():
        from lamapi.db_init import db_init
        db.create_all()
        db_init(db)

    @jwt.revoked_token_loader
    @jwt.needs_fresh_token_loader
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def invalid_token_callback(callback):
        response = make_response(json.dumps({ 'message': 'Invalid JWT Token.', 'mustReload': True }))
        unset_jwt_cookies(response)
        return response, 401

    @jwt.expired_token_loader
    def expired_token_callback(callback):
        response = make_response(json.dumps({ 'message': 'Expired JWT Token.', 'mustReload': True }))
        unset_access_cookies(response)
        return response, 401

    return app