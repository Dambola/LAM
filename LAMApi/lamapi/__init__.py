from flask import Flask, request
from flask_restful import Resource, Api
# from lamapi.db import DatabaseManager
from lamapi.config import LAMConfiguration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('lamapi.config.LAMConfiguration')
api = Api(app)
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()