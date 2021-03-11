from lamapi import db

class Music(db.Model):
    __tablename__ = 'musics'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    type1 = db.Column(db.Integer, nullable = False)
    type2 = db.Column(db.Integer, nullable = True)
    type3 = db.Column(db.Integer, nullable = True)
    db.UniqueConstraint(name, author)

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()
    
    def asJson(self):
        return self.id, {
            'name'   : self.name,
            'author' : self.author,
            'type1'  : self.type1,
            'type2'  : self.type2,
            'type3'  : self.type3,
        }