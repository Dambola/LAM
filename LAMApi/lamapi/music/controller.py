from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import get_jwt_identity, jwt_required

from lamapi.config import PermissionConfig as PC
from lamapi.music.model import Music
from lamapi.permission.model import Permission
from lamapi.music.parser import MusicPostParser, MusicPutParser
from lamapi import db

from sqlalchemy.exc import IntegrityError



class MusicController(Resource):
    
    # ---- TO-DO: Get Music
    @jwt_required
    def get(self):
        """Get method for the Music Resource.
        It will return a result of Music Query.

        Returns:
            dict: The json data.
            int: The HTTP code. (optional) 
        """

        # user = get_jwt_identity()
        musics = Music.query.all()
        if isinstance(musics, list):
            return { 'musics' : dict([ music.asJson() for music in musics ]) }, 200 
        return { 'message': 'Algum erro aconteceu.' }, 200
    
    @jwt_required
    def put(self):
        """Put method for the Music Resource.
        A music will be inserted.

        Returns:
            dict: The json data.
            int: The HTTP code. (optional) 
        """

        user = get_jwt_identity()
        
        if not Permission.hasPermission(user, PC.ADD_MUSIC):
            return { 'message': 'You don\'t have permission for music creation.' }, 401

        data = MusicPutParser.getArgs()

        name = data['name']
        author = data['author']
        type1 = data['type1']
        type2 = data.get('type2')
        type3 = data.get('type3')

        new_user = Music(name=name, author=author, type1=type1, type2=type2, type3=type3)
        try:
            new_user.doSave()
        except IntegrityError:
            return { 'message': f'Music {name} - {author} was already created.' }, 200
        except:
            return { 'message': 'An error occoured.' }, 500
            
        return { 'message': f'Music {name} - {author} was created.' }

    # ---- TO-DO: Update Music
    @jwt_required
    def post(self):
        """Put method for the Music Resource.
        A music will be inserted.

        Returns:
            dict: The json data.
            int: The HTTP code. (optional) 
        """

        user = get_jwt_identity()
        
        if not Permission.hasPermission(user, PC.EDT_MUSIC):
            return { 'message': 'You don\'t have permission for music edition.' }, 401

        data = MusicPostParser.getArgs()

        name   = data.get('name')
        author = data.get('author')
        type1  = data.get('type1')
        
        type2  = data.get('type2')
        type3  = data.get('type3')

        new_user = Music(name=name, author=author, type1=type1, type2=type2, type3=type3)
        try:
            new_user.doSave()
        except IntegrityError:
            return { 'message': f'Music {name} - {author} was already created.' }, 200
        except:
            return { 'message': 'An error occoured.' }, 500
        return { 'message': f'Music {name} - {author} was created.' }

    # ---- TO-DO: Delete Music
    @jwt_required
    def delete(self):
        return 'In progress (%s)...' % id
        