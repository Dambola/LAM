from flask import Flask, request
from flask_restful import Resource, Api
from lamapi.models import AuthorModel
from lamapi import db

class AuthorController(Resource):

    # ---- TO-DO: Get Music
    def get(self):
        authors = AuthorModel.query.all()
        if authors:
            return { 'authors' : dict([ author.asJSON() for author in authors ]) }, 200 
        return { 'message': 'Não foi possível achar músicas' }, 500
    
    # ---- TO-DO: Update Music
    def post(self):
        return 'In progress (%s)...' % id

    # ---- TO-DO: Delete Music
    def delete(self):
        return 'In progress (%s)...' % id
        