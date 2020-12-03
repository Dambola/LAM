from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from lamapi.config import LAMConfiguration


# Flask Basic Usage
app = Flask(__name__)
app.config.from_object('lamapi.config.LAMConfiguration')
config = app.config

# Extentions from Flask
api = Api(app)
db = SQLAlchemy(app)
cors = CORS(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    from lamapi.db_init import db_init
    db.create_all()
    db_init(db)