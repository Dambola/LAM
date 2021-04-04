from lamapi import db
from abc import ABCMeta

class DBInsert:
    __metaclass__ = ABCMeta

    def doInsert(self):
        error = None

        try:
            db.session.add(self)
            db.session.commit()
            db.session.refresh(self)
        except Exception as e:
            db.session.rollback()
            error = e
        finally:
            db.session.close()

        if error:
            raise error

class DBDelete:
    __metaclass__ = ABCMeta

    def doDelete(self):
        error = None

        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            error = e
        finally:
            db.session.close()

        if error:
            raise error

class DBUpdate:
    __metaclass__ = ABCMeta

    def doUpdate(self, changes):
        error = None

        for col in self.__table__.columns:
            if col.key in changes:
                setattr(self, col.key, changes[col.key])

        try:
            db.session.commit()
            db.session.refresh(self)
        except Exception as e:
            db.session.rollback()
            error = e
        finally:
            db.session.close()

        if error:
            raise error