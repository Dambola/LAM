class LAMConfiguration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://lamapi:ajZ88Xi2ojnxq9baEUhZDEqhaEPDxpJvkXcest6bkvEiH8fLnI@localhost/louvoragapemontese'
    SECRET_KEY = 'kjqOQXTvEgd1Aj2JyZ5x7SRgS49J60n0qF0w3uEG0nyCa5KqmCt19CZIGzbp'
    JWT_SECRET_KEY = 'super-secret'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True
    SESSION_COOKIE_SECURE = True
    ALGORITHM = 'HS256'

class PermissionConfig(object):
    ADD_MUSIC = 0
    ADD_MUSIC_LABEL = "Adicionar Música"
    ADD_MUSIC_DESC = "Permissão para adicionar músicas do repertório."
    EDT_MUSIC = 1
    EDT_MUSIC_LABEL = "Editar Música"
    EDT_MUSIC_DESC = "Permissão para Editar músicas do repertório."
    DEL_MUSIC = 2
    DEL_MUSIC_LABEL = "Remover Música"
    DEL_MUSIC_DESC = "Remover para adicionar músicas do repertório."
