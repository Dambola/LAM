from flask import make_response
from flask_jwt_extended import unset_access_cookies, \
    unset_jwt_cookies

from lamapi.setup import setupFlaskApplication, \
    setupFlaskExtensions, setupFlaskResources

import json

app = setupFlaskApplication()
api, db, cors, jwt = setupFlaskExtensions(app)
setupFlaskResources(api)

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
    # Invalid Fresh/Non-Fresh Access token in auth header
    print('f')
    response = make_response(json.dumps({ 'message': 'Invalid JWT Token.', 'mustReload': True }))
    unset_jwt_cookies(response)
    return response, 401

@jwt.expired_token_loader
def expired_token_callback(callback):
    # Expired auth header
    response = make_response(json.dumps({ 'message': 'Expired JWT Token.', 'mustReload': True }))
    unset_access_cookies(response)
    return response, 401