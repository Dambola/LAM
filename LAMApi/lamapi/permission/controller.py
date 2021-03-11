from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import get_jwt_identity, jwt_required
from lamapi.models import TypeModel, Permission
from lamapi import db


class PermissionController(Resource):

    # ---- TO-DO: Get Permission
    @jwt_required
    def get(self):
        user = get_jwt_identity()
        perms = Permission.getPermissions(user)
        return { 'permissions' : perms }, 200 
    
    # ---- TO-DO: Update Permission
    @jwt_required
    def post(self):
        return 'In progress (%s)...' % id
    
    # ---- TO-DO: Insert Permission
    @jwt_required
    def put(self):
        return 'In progress (%s)...' % id

    # ---- TO-DO: Delete Permission
    @jwt_required
    def delete(self):
        return 'In progress (%s)...' % id