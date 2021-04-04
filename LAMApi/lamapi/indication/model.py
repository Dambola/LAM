from lamapi import db
from lamapi.music.model import MusicManager
from lamapi.utils.db import DBInsert, DBDelete, DBUpdate
from lamapi.utils.api import SingletonMeta
from lamapi.indication.constants import OrderBy, FilterBy
from lamapi.indication.exception import *

from sqlalchemy import or_

class IndicationManager(metaclass=SingletonMeta):

    class __MetaIndication(db.Model, DBInsert, DBDelete, DBUpdate):
        __tablename__ = 'indications'

        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        name = db.Column(db.String(100), nullable = False)
        author = db.Column(db.String(100), nullable = False)
        type1 = db.Column(db.Integer, nullable = False)
        type2 = db.Column(db.Integer, nullable = True)
        type3 = db.Column(db.Integer, nullable = True)
        user = db.Column(db.Integer, nullable = False)
        link = db.Column(db.String(150), nullable = True)
        db.UniqueConstraint(name, author)

        def asJSON(self):
            return {
                'id'     : self.id,
                'name'   : self.name,
                'author' : self.author,
                'type1'  : self.type1,
                'type2'  : self.type2,
                'type3'  : self.type3,
                'user'   : self.user,
                'link'   : self.link,
            }
    __meta = __MetaIndication

    _filtersOperation = {
        FilterBy.Key.Name: lambda self, x: self.__meta.name.in_(x),
        FilterBy.Key.Author: lambda self, x: self.__meta.author.in_(x),
        FilterBy.Key.User: lambda self, x: self.__meta.user.in_(x),
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
        OrderBy.User.Asc: lambda self: self.__meta.user.asc(),
        OrderBy.User.Desc: lambda self: self.__meta.user.desc(),
    }


    # ---- Public methods
    
    def add(self, indication):
        self.__validateJSON(indication)
        json = self.__toJSON(indication)
        object = self.__meta(**json)
        return self.__doInsert(object)
    
    def edit(self, indication_id: int, indication: dict):
        self.__validateJSON(indication)
        json = self.__toJSON(indication)
        object = self.__meta.query \
            .filter_by(id=indication_id) \
            .first()
        return self.__doUpdate(object, indication)

    def approve(self, indication_id: int):
        object = self.__meta.query \
            .filter_by(id=indication_id) \
                .first()

        if not object:
            return None, IndicationNotFound

        mgr = MusicManager()
        json = object.asJSON()
        music_id, error = mgr.add(json)

        if not music_id:
            return None, error
        
        done, error = self.__doDelete(object)
        if not done:
            return music_id, IndicationNotDeleted

        return done, error

    def delete(self, indication_id: int):
        object = self.__meta.query \
            .filter_by(id=indication_id) \
                .first()
        return self.__doDelete(object)


    # -------- Search methods

    def searchByID(self, indication_id: int):
        indication = self.__meta.query \
            .filter_by(id=indication_id) \
                .first()
        if indication:
            return indication.asJSON()
        return None
    
    def searchByName(self, name: str, author: str):
        indication = self.__meta.query \
            .filter_by(name=name, author=author) \
                .first()
        if indication:
            return indication.asJSON()
        return None
    
    def searchAll(self, filter_by: list = [], order_by: list = []) -> list:
        filters = self.__getFilters(filter_by)
        orders = self.__getOrders(order_by)
        objects = self.__meta \
            .query \
            .filter(*filters) \
            .order_by(*orders) \
            .all()
        
        return [ obj.asJSON() for obj in objects ]

    
    # ---- Internal methods
    
    def __toJSON(self, indication):
        return {
            'name': indication.get('name'),
            'author': indication.get('author'),
            'type1': indication.get('type1'),
            'type2': indication.get('type2'),
            'type3': indication.get('type3'),
            'user': indication.get('user'),
            'link': indication.get('link'),
        }
    
    def __validateJSON(self, indication):
        if not isinstance(indication, dict):
            raise NotValidIndicationJSONFormat

        if 'name' not in indication:
            raise NotValidIndicationJSONName

        if 'author' not in indication:
            raise NotValidIndicationJSONAuthor

        if 'type1' not in indication:
            raise NotValidIndicationJSONType1

        if 'type2' not in indication:
            raise NotValidIndicationJSONType2

        if 'type3' not in indication:
            raise NotValidIndicationJSONType3

        if 'user' not in indication:
            raise NotValidIndicationJSONUser

        if 'link' not in indication:
            raise NotValidIndicationJSONUser
 
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

    def __doInsert(self, object: __MetaIndication):
        try:
            object.doInsert()
            return object.id, None
        except Exception as e:
            return None, e
    
    def __doDelete(self, object: __MetaIndication):
        try:
            object.doDelete()
            return True, None
        except Exception as e:
            return False, e
    
    def __doUpdate(self, object: __MetaIndication, changes: dict):
        try:
            object.doUpdate(changes)
            return True, None
        except Exception as e:
            raise e
            return False, e
