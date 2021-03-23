from lamapi import db

class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False, unique = True)

    def doSave(self):
        db.session.add(self)
        db.session.commit()
    
    def asJson(self):
        return self.id, {
            'name'   : self.name
        }