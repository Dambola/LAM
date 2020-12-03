from lamapi import db
from lamapi.models import User

class Permission(db.Model):
    __tablename__ = 'permission'

    permission = db.Column(db.Integer, primary_key = True, nullable = False)
    user = db.Column(db.Integer, primary_key = True, nullable = False)
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_permissions(cls, login):
        user_id = User.get_user_id(login)
        return [perm.permission for perm in cls.query.filter_by(user=user_id).all()]

    @classmethod
    def has_permission(cls, user, perm):
        perm = cls.query.filter_by(user=user, permission=perm).first()
        return perm is not None
    
    def asJSON(self):
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
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
    
    def asJSON(self):
        return {
            'id'          : self.id,
            'name'        : self.name,
            'description' : self.description,
        }