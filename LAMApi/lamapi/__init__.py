from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, unset_access_cookies, \
    unset_jwt_cookies

from lamapi.config import LAMConfiguration

import json


# Flask Basic Usage
app = Flask(__name__)
app.config.from_object('lamapi.config.LAMConfiguration')
config = app.config

# Extentions from Flask
api = Api(app)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    from lamapi.db_init import db_init
    db.create_all()
    db_init(db)

@jwt.invalid_token_loader
def invalid_token_callback(callback):
    # Invalid Fresh/Non-Fresh Access token in auth header
    response = make_response(json.dumps({ 'msg': 'Invalid JWT Token.' }))
    unset_jwt_cookies(response)
    return response, 401

@jwt.expired_token_loader
def expired_token_callback(callback):
    # Expired auth header
    response = make_response(json.dumps({ 'msg': 'Expired JWT Token.' }))
    unset_access_cookies(response)
    return response, 401