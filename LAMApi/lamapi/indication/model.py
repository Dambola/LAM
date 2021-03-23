from lamapi import db
from lamapi.music.model import Music
from lamapi.utils.db import DbBasicOperations
from lamapi.utils.api import SingletonMeta
from lamapi.indication.exception import NotValidIndication

from sqlalchemy import or_, and_

class IndicationManager(metaclass=SingletonMeta):

    class __MetaIndication(db.Model, DbBasicOperations):
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
    
    __meta = __MetaIndication
    
    def addIndication(self, indication):
        if not isinstance(indication, dict):
            raise NotValidIndication('Indication must be a dict type.')

        if 'name' not in indication:
            raise NotValidIndication('Name not found in indication.')

        if 'author' not in indication:
            raise NotValidIndication('Author not found in indication.')

        if 'type1' not in indication:
            raise NotValidIndication('Type 1 not found in indication.')

        if 'user' not in indication:
            raise NotValidIndication('User not found in indication.')
        
        kwargs = {
            'name': indication.get('name'),
            'author': indication.get('author'),
            'type1': indication.get('type1'),
            'type2': indication.get('type2'),
            'type3': indication.get('type3'),
            'user': indication.get('user'),
            'link': indication.get('link'),
        }

        obj = self.__meta(**kwargs)

        try:
            obj.doSave()
            obj_id = obj.id
        except Exception as e:
            obj_id = None

        return obj_id
    
    def approveIndication(self, indication_id: int):
        indication = self.getAnIndication(indication_id)

        if not indication:
            raise Exception(str(indication_id))
            return False

        try:
            music = Music(
                name=indication.name, 
                author=indication.author, 
                type1=indication.type1,
                type2=indication.type2,
                type3=indication.type3,
            )
            music.doSave()
        except Exception as e:
            raise e
            return False
        
        obj = self.__meta.query.filter_by(id=indication_id).first()
        
        try:
            obj.doDelete()
        except Exception as e:
            raise e
            return False

        return True

    def refuseIndication(self, indication_id: int):
        indication = self.getAnIndication(indication_id)

        if not indication:
            return False
        
        obj = self.__meta.query.filter_by(id=indication_id).first()
        
        try:
            obj.doDelete()
        except:
            return False

        return True

    def getAllIndications(self, *args):
        clauses = []
        
        for arg in args:
            if not isinstance(arg, dict):
                continue
            
            clause = []

            name = arg.get('name')
            author = arg.get('author')
            type1 = arg.get('type1')
            type2 = arg.get('type2')
            type3 = arg.get('type3')
            user = arg.get('user')
            link = arg.get('link')
                
            if name: clause.append(self.__meta.name == name)
            if author: clause.append(self.__meta.author == author)
            if type1: clause.append(self.__meta.type1 == type1)
            if type2: clause.append(self.__meta.type2 == type2)
            if type3: clause.append(self.__meta.type3 == type3)
            if user: clause.append(self.__meta.user == user)
            if link: clause.append(self.__meta.link == link)

            clauses.append(and_(*clause))
        
        return self.__meta.query.filter(or_(*clauses)).all()

    def getAnIndication(self, indication):
        if isinstance(indication, int):
            return self.__meta.query.filter_by(id=indication).first()

        elif isinstance(indication, dict):
            if 'name' not in indication:
                raise NotValidIndication('Name not found in indication.')

            if 'author' not in indication:
                raise NotValidIndication('Author not found in indication.')

            if 'type1' not in indication:
                raise NotValidIndication('Type 1 not found in indication.')

            if 'user' not in indication:
                raise NotValidIndication('User not found in indication.')

            kwargs = {
                'name': indication.get('name'),
                'author': indication.get('author'),
                'type1': indication.get('type1'),
                'type2': indication.get('type2'),
                'type3': indication.get('type3'),
                'user': indication.get('user'),
                'link': indication.get('link'),
            }

            return self.__meta.query.filter_by(**kwargs).first()
        return None

    
        