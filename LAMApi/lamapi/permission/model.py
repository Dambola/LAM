from lamapi import db
from lamapi.auth.model import User

class Permission(db.Model):
    __tablename__ = 'permission'

    permission = db.Column(db.Integer, primary_key = True, nullable = False)
    user = db.Column(db.Integer, primary_key = True, nullable = False)
    
    def saveToDb(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def getPermissions(cls, login):
        user_id = User.getUserId(login)
        return [perm.permission for perm in cls.query.filter_by(user=user_id).all()]

    @classmethod
    def hasPermission(cls, login, perm):
        user_id = User.getUserId(login)
        perm = cls.query.filter_by(user=user_id, permission=perm).first()
        return perm is not None
    
    def asJson(self):
        return {
            'user'    : self.user,
            'permission' : self.permission
        }

class PermissionConfig(db.Model):
    __tablename__ = 'permission_config'

    id = db.Column(db.Integer, primary_key = True, autoincrement = False)
    name = db.Column(db.String(120), unique = True, nullable = False)
    label = db.Column(db.String(120), nullable = False)
    description = db.Column(db.String(340), nullable = False)
    
    def saveToDb(self):
        db.session.add(self)
        db.session.commit()
    
    def asJson(self):
        return {
            'id'          : self.id,
            'name'        : self.name,
            'description' : self.description,
        }