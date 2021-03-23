from flask import Flask, request
from flask_restful import Resource, Api

from lamapi.type.model import Type
from lamapi import db

class TypeController(Resource):

    # ---- TO-DO: Get Music
    def get(self):
        types = Type.query.all()
        if types:
            return { 'types' : dict([ type.asJson() for type in types ]) }, 200 
        return { 'message': 'Não foi possível achar músicas' }, 500
    
    # ---- TO-DO: Update Music
    def post(self):
        return 'In progress (%s)...' % id

    # ---- TO-DO: Delete Music
    def delete(self):
        return 'In progress (%s)...' % id
        