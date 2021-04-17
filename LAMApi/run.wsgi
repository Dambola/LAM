class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://lam_user:Gi0qolC3P6KTXXdWnfZ41WTzE0mPuGc2pSiU5lNLhZf4w9QZepSWCnLGdyXO5zGkIo5DPIOyhtsTs9sNpCjrquzKjLZeAfEJK9Mb@172.17.0.2/louvor_agape_montese'
    SECRET_KEY = 'kjqOQXTvEgd1Aj2JyZ5x7SRgS49J60n0qF0w3uEG0nyCa5KqmCt19CZIGzbp'
    JWT_SECRET_KEY = 'super-secret'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_CSRF_CHECK_FORM = False
    SESSION_COOKIE_SECURE = True
    ALGORITHM = 'HS256'

from lamapi import createApplication
application = createApplication(Config)