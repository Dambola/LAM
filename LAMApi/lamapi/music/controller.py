from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import get_jwt_identity, jwt_required

from lamapi.config import PermissionConfig as PC
from lamapi.music.model import MusicManager
from lamapi.permission.model import Permission
from lamapi.music.parser import *
from lamapi import db

from sqlalchemy.exc import IntegrityError



class MusicController(Resource):
    
    def get(self):
        """Get method for the Music Resource.
        It will return a result of Music Query.

        Returns:
            dict: The json data.
            int: The HTTP code. (optional) 
        """

        mgr = MusicManager()
        parser = MusicGetParser()

        data = parser.getArgs()
        musics = mgr.searchAll()

        if isinstance(musics, list):
            return { 'musics' : musics }

        return { 'message': 'Algum erro aconteceu.' }, 500
    
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

        mgr = MusicManager()
        parser = MusicPutParser()

        data = parser.getArgs()
        music_id, error = mgr.add(data)
        
        if music_id and not error:
            return { 'id': music_id, 'message': f'Music was created.' }

        if error == IntegrityError:
            return { 'message': f'Music was already created.' }, 500
            
        return { 'message': 'An error occoured.' }, 500
        
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

        mgr = MusicManager()
        parser = MusicPostParser()

        data = parser.getArgs()
        edited, error = mgr.edit(data['id'], data)

        if edited and not error:
            return { 'message': f'Music was edited.' }
        
        return { 'message': 'An error occoured.' }, 500

    @jwt_required
    def delete(self):
        """Delete method for the Music Resource.
        A music will be delete.

        Returns:
            dict: The json data.
            int: The HTTP code. (optional) 
        """

        user = get_jwt_identity()
        
        if not Permission.hasPermission(user, PC.DEL_MUSIC):
            return { 'message': 'You don\'t have permission for music deletion.' }, 401

        mgr = MusicManager()
        parser = MusicDeleteParser()

        data = parser.getArgs()
        deleted, error = mgr.remove(data['id'])
        
        if deleted and not error:
            return { 'message': f'Music was deleted.' }
            
        return { 'message': 'An error occoured.' }, 500
        