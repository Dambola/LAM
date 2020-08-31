from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import get_jwt_identity, jwt_required, get_current_user

from lamapi.models import MusicModel
from lamapi import db


class MusicController(Resource):

    # ---- TO-DO: Get Music
    @jwt_required
    def get(self):
        user = get_jwt_identity()
        musics = MusicModel.query.all()

        if isinstance(musics, list):
            return { 'musics' : dict([ music.asJSON() for music in musics ]) }, 200 
        return { 'msg': 'Algum erro aconteceu.' }, 200
    
    # ---- TO-DO: Update Music
    def post(self):
        return 'In progress (%s)...' % id

    # ---- TO-DO: Delete Music
    def delete(self):
        return 'In progress (%s)...' % id
        