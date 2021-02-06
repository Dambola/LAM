from lamapi import db

class TypeModel(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False, unique = True)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def asJSON(self):
        return self.id, {
            'name'   : self.name
        }