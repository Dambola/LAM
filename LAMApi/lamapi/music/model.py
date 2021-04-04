from lamapi import db
from lamapi.utils.db import DBInsert, DBDelete, DBUpdate
from lamapi.utils.api import SingletonMeta
from lamapi.music.constants import OrderBy, FilterBy
from lamapi.music.exception import *

from sqlalchemy import or_

class MusicManager(metaclass=SingletonMeta):

    class __MetaMusic(db.Model, DBInsert, DBDelete, DBUpdate):
        __tablename__ = 'musics'

        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        name = db.Column(db.String(100), nullable = False)
        author = db.Column(db.String(100), nullable = False)
        type1 = db.Column(db.Integer, nullable = False)
        type2 = db.Column(db.Integer, nullable = True)
        type3 = db.Column(db.Integer, nullable = True)
        db.UniqueConstraint(name, author)

        def asJSON(self):
            return {
                'id'     : self.id,
                'name'   : self.name,
                'author' : self.author,
                'type1'  : self.type1,
                'type2'  : self.type2,
                'type3'  : self.type3,
            }
    __meta = __MetaMusic
   
    _filtersOperation = {
        FilterBy.Key.Name: lambda self, x: self.__meta.name.in_(x),
        FilterBy.Key.Author: lambda self, x: self.__meta.author.in_(x),
        FilterBy.Key.Type: lambda self, x: or_(
                self.__meta.type1.in_(x),
                self.__meta.type2.in_(x),
                self.__meta.type3.in_(x)
            )
    }

    __ordersOperation = {
        OrderBy.Id.Asc: lambda self: self.__meta.id.asc(),
        OrderBy.Id.Desc: lambda self: self.__meta.id.desc(),
        OrderBy.Name.Asc: lambda self: self.__meta.name.asc(),
        OrderBy.Name.Desc: lambda self: self.__meta.name.desc(),
        OrderBy.Author.Asc: lambda self: self.__meta.author.asc(),
        OrderBy.Author.Desc: lambda self: self.__meta.author.desc(),
    }


    # ---- Public methods

    def add(self, music: dict):
        """This method will create a music based on the
        music JSON type.

        Args:
            music (dict): Music JSON definied as a json.

        Returns:
            (id, error): New music ID if created otherwise None.
        """        

        self.__validateJSON(music)
        json = self.__toJSON(music)
        object = self.__meta(**json)
        return self.__doInsert(object)

    def remove(self, music_id: int):
        """This method will delete a music based on the
        music ID.

        Args:
            music_id (int): The music ID to be deleted.

        Returns:
            (music, error): True if removed otherwise None.
        """        

        object = self.__meta.query \
            .filter_by(id=music_id) \
                .first()
        return self.__doDelete(object)

    def edit(self, music_id: int, music: dict):
        """This method will edit a music based on the
        music JSON type.

        Args:
            music_id (int): The music ID to be edited.
            music (dict): Music JSON definied as a json.

        Returns:
            (id, error): New music ID if created otherwise None.
        """

        self.__validateJSON(music)
        json = self.__toJSON(music)
        object = self.__meta.query \
            .filter_by(id=music_id) \
            .first()
        return self.__doUpdate(object, music)


    # -------- Search methods

    def searchByID(self, music_id: int):
        """This method will search a music by the
        ID of the song.

        Args:
            music_id (int): The ID of the searched music.

        Returns:
            (dict): Music as JSON if exists otherwise None.
        """

        music = self.__meta.query \
            .filter_by(id=music_id) \
                .first()
        if music:
            return music.asJSON()
        return None

    def searchByName(self, name: str, author: str):
        """This method will search a music by the
        name and the author of the song.

        Args:
            name (str): The name of the searched music.
            author (str): The author of the searched music.

        Returns:
            (dict): Music as JSON if exists otherwise None.
        """

        music = self.__meta.query \
            .filter_by(name=name, author=author) \
                .first()
        if music:
            return music.asJSON()
        return None

    def searchAll(self, filter_by: list = [], order_by: list = []) -> list:
        """This method will search all musics filtered 
        by a given filter and ordered by a given order.

        Args:
            filter_by (list, optional): List of filters with FilterBy scope. Defaults to [].
            order_by (list, optional): List of filters with OrderBy scope. Defaults to [].

        Returns:
            list: A list of musics as JSON.
        """          

        filters = self.__getFilters(filter_by)
        orders = self.__getOrders(order_by)
        objects = self.__meta \
            .query \
            .filter(*filters) \
            .order_by(*orders) \
            .all()
        
        return [ obj.asJSON() for obj in objects ]
    

    # ---- Internal methods

    def __toJSON(self, music):
        if not isinstance(music, dict):
            raise NotValidMusicJSONFormat

        return {
            'name': music.get('name'),
            'author': music.get('author'),
            'type1': music.get('type1'),
            'type2': music.get('type2'),
            'type3': music.get('type3')
        }
    
    def __validateJSON(self, music):  
        
        if not isinstance(music, dict):
            raise NotValidMusicJSONFormat

        if 'name' not in music:
            raise NotValidMusicJSONName

        if 'author' not in music:
            raise NotValidMusicJSONAuthor

        if 'type1' not in music:
            raise NotValidMusicJSONType1
        
        if 'type2' not in music:
            raise NotValidMusicJSONType2
        
        if 'type3' not in music:
            raise NotValidMusicJSONType3

    def __getFilters(self, filter_by: list):
        filters = []

        for f in filter_by:
            key = f.get('key')
            values = f.get('values')

            if not key or not values:
                continue
            
            operation = self._filtersOperation.get(key, lambda self, _ : None)
            constraint = operation(self, values)
            
            if constraint is not None:
                filters.append(constraint)
        
        return filters
    
    def __getOrders(self, order_by: list):
        orders = []

        for o in order_by:
            operation = self.__ordersOperation.get(o, lambda self: None)
            constraint = operation(self)
            
            if constraint is not None:
                orders.append(constraint)
        
        return orders


    # -------- Meta methods

    def __doInsert(self, object: __MetaMusic) :
        try:
            object.doInsert()
            return object.id, None
        except Exception as e:
            return None, e
    
    def __doDelete(self, object: __MetaMusic):
        try:
            object.doDelete()
            return True, None
        except Exception as e:
            return False, e
    
    def __doUpdate(self, object: __MetaMusic, changes: dict):
        try:
            object.doUpdate(changes)
            return True, None
        except Exception as e:
            raise e
            return False, e
