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

        def asJson(self):
            return self.id, {
                'name'   : self.name,
                'author' : self.author,
                'type1'  : self.type1,
                'type2'  : self.type2,
                'type3'  : self.type3,
                'user'   : self.user,
                'link'   : self.link,
            }
    
    __meta = __MetaIndication
    
    def addIndication(self, indication):
        self.__validateIndicationDict(indication)
        kwargs = self.__dictToKwargs(indication)
        meta_object = self.__meta(**kwargs)
        return self.__doSave(meta_object)
    
    def approveIndication(self, indication_id: int):
        indication = self.getAnIndication(indication_id)

        if not indication:
            return False

        self.__createMusic(indication)

        meta_object = self.__meta.query.filter_by(id=indication_id).first()
        return self.__doDelete(meta_object)

    def refuseIndication(self, indication_id: int):
        indication = self.getAnIndication(indication_id)

        if not indication:
            return False
        
        meta_object = self.__meta.query.filter_by(id=indication_id).first()
        return self.__doDelete(meta_object)

    def getAllIndications(self, *args):
        clauses = []
        
        for arg in args:
            if not isinstance(arg, dict):
                continue
            
            clause = []

            kwargs = self.__dictToKwargs(arg)
                
            if kwargs['name']: clause.append(self.__meta.name == kwargs['name'])
            if kwargs['author']: clause.append(self.__meta.author == kwargs['author'])
            if kwargs['type1']: clause.append(self.__meta.type1 == kwargs['type1'])
            if kwargs['type2']: clause.append(self.__meta.type2 == kwargs['type2'])
            if kwargs['type3']: clause.append(self.__meta.type3 == kwargs['type3'])
            if kwargs['user']: clause.append(self.__meta.user == kwargs['user'])
            if kwargs['link']: clause.append(self.__meta.link == kwargs['link'])

            clauses.append(and_(*clause))
        
        return self.__meta.query.filter(or_(*clauses)).all()

    def getAnIndication(self, indication):
        operator = self.__getNoneIndication
        if isinstance(indication, int):
            operator = self.__getAnIndicationAsInt
        elif isinstance(indication, dict):
            operator = self.__getAnIndicationAsDict
        return operator(indication)
    

    # ---- Internal methods
    
    def __dictToKwargs(self, _dict):
        return {
            'name': _dict.get('name'),
            'author': _dict.get('author'),
            'type1': _dict.get('type1'),
            'type2': _dict.get('type2'),
            'type3': _dict.get('type3'),
            'user': _dict.get('user'),
            'link': _dict.get('link'),
        }
    
    def __validateIndicationDict(self, _dict):
        if not isinstance(_dict, dict):
            raise NotValidIndication('Indication must be a dict type.')

        if 'name' not in _dict:
            raise NotValidIndication('Name not found in indication.')

        if 'author' not in _dict:
            raise NotValidIndication('Author not found in indication.')

        if 'type1' not in _dict:
            raise NotValidIndication('Type 1 not found in indication.')

        if 'user' not in _dict:
            raise NotValidIndication('User not found in indication.')
        
    def __getAnIndicationAsInt(self, indication: int):
        return self.__meta.query.filter_by(id=indication).first()

    def __getAnIndicationAsDict(self, indication: dict):
        self.__validateIndicationDict(indication)
        kwargs = self.__dictToKwargs(indication)
        return self.__meta.query.filter_by(**kwargs).first()

    def __getNoneIndication(self, indication):
        return None

    def __createMusic(self, indication: __MetaIndication):
        _id, _dict = indication.asJson()
        music_cols = ['name', 'author', 'type1', 'type2', 'type3']
        kwargs = {key: value for key, value in _dict.items() if key in music_cols}
        
        try:
            music = Music(**kwargs)
            music.doSave()

        except Exception as e:
            return False
    

    # ---- Meta methods

    def __doSave(self, indication: __MetaIndication) :
        try:
            indication.doSave()
            return indication.id
        except Exception as e:
            return None
    
    def __doDelete(self, indication: __MetaIndication):
        try:
            indication.doDelete()
            return True
        except Exception as e:
            return False
