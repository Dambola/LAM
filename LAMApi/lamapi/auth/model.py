from lamapi import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    login = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    name = db.Column(db.String(120))
    smallname = db.Column(db.String(120))
    birthdate = db.Column(db.Date())

    @classmethod
    def get_user_id(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user.id
        return None

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def asJSON(self):
        return {
            'id'       : self.id,
            'login'    : self.login,
            'password' : self.password,
            'email'    : self.email,
        }