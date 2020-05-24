from flask import Flask, request
from flask_restful import Resource, Api
from lamapi.db import DatabaseManager

app = Flask(__name__)
api = Api(app)
db = DatabaseManager('localhost', 'root', password='abcd1234', db='louvoragapemontese')