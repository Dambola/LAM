from flask import Flask, request
from flask_restful import Resource, Api
from lamapi.models import MusicModel, TypeModel, AuthorModel
from lamapi import db

class MusicGeneralController(Resource):

    # ---- TO-DO: Get Music
    def get(self):
        return 'In progress...'

    # ---- TO-DO: Insert Music
    def put(self):
        return 'In progress...'

class MusicController(Resource):
    # ---- TO-DO: Get Music
    def get(self, id):
        return 'In progress (%s)...' % id
    
    # ---- TO-DO: Update Music
    def post(self, id):
        return 'In progress (%s)...' % id

    # ---- TO-DO: Delete Music
    def delete(self, id):
        return 'In progress (%s)...' % id
        