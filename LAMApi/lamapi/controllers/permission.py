from flask import Flask, request
from flask_restful import Resource, Api
from lamapi.models import TypeModel
from lamapi import db

class PermissionController(Resource):

    # ---- TO-DO: Get Music
    def get(self):
        if '':
            return { 'permissions' : []}, 200 
        return { 'permissions': [] }, 200
        # return { 'message': 'Não foi possível achar músicas' }, 500
    
    # ---- TO-DO: Update Music
    def post(self):
        return 'In progress (%s)...' % id

    # ---- TO-DO: Delete Music
    def delete(self):
        return 'In progress (%s)...' % id
        