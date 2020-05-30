from flask import Flask, request
from flask_restful import Resource, Api
from lamapi.models import MusicModel, TypeModel, AuthorModel
from lamapi import db

class MusicGeneralController(Resource):
    def get(self):
        page = request.args.get('page','1')
        orderby = request.args.get('orderby','name')
        
        
        db.connect()
        musics = MusicModel.query(db)
        authorsIds = set()
        typesIds = set()
        for music in musics:
            authorsIds.add(str(music.author))
            typesIds.add(str(music.type1))
            if music.type2:
                typesIds.add(str(music.type2))
            if music.type3:
                typesIds.add(str(music.type3))
        authors = AuthorModel.query(db,where='`id` IN (%s)' % (','.join(authorsIds)))
        types = TypeModel.query(db,where='`id` IN (%s)' % (','.join(typesIds)))
        db.close()
        
        return {
            'authors' : {author.id : author.as_json() for author in authors},
            'musics' : [music.as_json() for music in musics],
            'types' : {type.id : type.as_json() for type in types},
            'orderby' : orderby,
            'page' : page
        }

    # --- TO-DO: Insert Music
    def put(self):
        return 'In progress...'

class MusicController(Resource):
    # --- TO-DO: Get Music
    def get(self, id):
        return 'In progress (%s)...' % id
    
    # --- TO-DO: Update Music
    def post(self, id):
        return 'In progress (%s)...' % id

    # --- TO-DO: Delete Music
    def delete(self, id):
        return 'In progress (%s)...' % id


''' 
TO-DO:
-   Create the MusicGeneralController 'Get' Resource for get Musics (missing limit pagination)
-   Create the MusicGeneralController 'Put' Resource for Creating new Musics
-   Create the MusicController 'Get' Resource to get a Specific music from /music/id
-   Create the MusicController 'Post' Resource to update a Specific music from /music/id
-   Create the MusicController 'Delete' Resource to delete a Specific music from /music/id
'''