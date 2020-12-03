from lamapi.config import PermissionConfig as PC
from lamapi.models.permission import PermissionConfig as PCM

from sqlalchemy.exc import IntegrityError

def db_init(db):
    permissions = [
        PCM(id=PC.ADD_MUSIC, 
        name='ADD_MUSIC', 
        label=PC.ADD_MUSIC_LABEL, 
        description=PC.ADD_MUSIC_DESC),

        PCM(id=PC.EDT_MUSIC, 
        name='EDT_MUSIC', 
        label=PC.EDT_MUSIC_LABEL, 
        description=PC.EDT_MUSIC_DESC),

        PCM(id=PC.DEL_MUSIC, 
        name='DEL_MUSIC', 
        label=PC.DEL_MUSIC_LABEL, 
        description=PC.DEL_MUSIC_DESC),
    ]

    for perm in permissions:
        db.session.merge(perm)
    db.session.commit()        
        