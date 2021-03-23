from lamapi import db

class DbBasicOperations:
    def doSave(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
    
    def doDelete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
    
    def asJson(self):
        return self.id, {
            'name'   : self.name,
            'author' : self.author,
            'type1'  : self.type1,
            'type2'  : self.type2,
            'type3'  : self.type3,
        }