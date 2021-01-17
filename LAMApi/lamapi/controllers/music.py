from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from flask_jwt_extended import get_jwt_identity, jwt_required

from lamapi.config import PermissionConfig as PC
from lamapi.models import Music, Permission
from lamapi import db

from sqlalchemy.exc import IntegrityError

put_music_parser = RequestParser()
put_music_parser.add_argument('name', help = 'Este campo é obrigatório', required = True)
put_music_parser.add_argument('author', help = 'Este campo é obrigatório', required = True)
put_music_parser.add_argument('type1', help = 'Este campo é obrigatório', required = True)
put_music_parser.add_argument('type2')
put_music_parser.add_argument('type3')

post_music_parser = RequestParser()
post_music_parser.add_argument('id', help = 'Este campo é obrigatório', required = True)
post_music_parser.add_argument('name')
post_music_parser.add_argument('author')
post_music_parser.add_argument('type1')
post_music_parser.add_argument('type2')
post_music_parser.add_argument('type3')

class MusicController(Resource):

    # ---- TO-DO: Get Music
    # @jwt_required
    def get(self):
        # user = get_jwt_identity()
        musics = Music.query.all()
        if isinstance(musics, list):
            return { 'musics' : dict([ music.asJSON() for music in musics ]) }, 200 
        return { 'msg': 'Algum erro aconteceu.' }, 200
    
    # ---- TO-DO: Insert Music
    @jwt_required
    def put(self):
        """TO-DO: Must create documentation here"""
        user = get_jwt_identity()
        if not Permission.has_permission(user, PC.ADD_MUSIC):
            return { 'msg': 'You don\'t have permission for that.' }, 401

        data = put_music_parser.parse_args()

        name = data['name']
        author = data['author']
        type1 = data['type1']
        type2 = data.get('type2')
        type3 = data.get('type3')

        new_user = Music(name=name, author=author, type1=type1, type2=type2, type3=type3)
        try:
            new_user.saveToDB()
        except IntegrityError:
            return { 'msg': f'Music {name} - {author} was already created.' }, 200
        except:
            return { 'msg': 'An error occoured.' }, 500
        return { 'msg': f'Music {name} - {author} was created.' }

    # ---- TO-DO: Update Music
    @jwt_required
    def post(self):
        """TO-DO: Must create documentation here"""
        user = get_jwt_identity()
        if not Permission.has_permission(user, PC.EDT_MUSIC):
            return { 'msg': 'You don\'t have permission for that.' }, 401

        data = post_music_parser.parse_args()

        name   = data.get('name')
        author = data.get('author')
        type1  = data.get('type1')
        type2  = data.get('type2')
        type3  = data.get('type3')

        new_user = Music(name=name, author=author, type1=type1, type2=type2, type3=type3)
        try:
            new_user.saveToDB()
        except IntegrityError:
            return { 'msg': f'Music {name} - {author} was already created.' }, 200
        except:
            return { 'msg': 'An error occoured.' }, 500
        return { 'msg': f'Music {name} - {author} was created.' }

    # ---- TO-DO: Delete Music
    @jwt_required
    def delete(self):
        return 'In progress (%s)...' % id
        