from lamapi import db

class DbBasicOperations(object):
    def doSave(self):
        try:
            db.session.add(self)
            db.session.flush()
            db.session.commit()
            db.session.refresh(self)
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
    
    def doDelete(self):
        try:
            db.session.refresh(self)
            db.session.delete(self)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()