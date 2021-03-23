from lamapi import db
from lamapi.utils.db import DbBasicOperations
from lamapi.utils.api import SingletonMeta

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
        pass
    
    def approveIndication(self, indication_id: int):
        pass

    def refuseIndication(self, indication_id: int):
        pass

    def getAllIndications(self, *args):
        pass

    def getAnIndication(self, indication):
        pass

    
        