from flask import Flask, request
from flask_restful import Resource, Api
from lamapi.db import DatabaseManager
from lamapi.config import DATABASE_HOST, \
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_SCHEMA

app = Flask(__name__)
api = Api(app)
db = DatabaseManager(DATABASE_HOST, DATABASE_USER, password=DATABASE_PASSWORD, db=DATABASE_SCHEMA)