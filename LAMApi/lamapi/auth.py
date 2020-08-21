from lamapi import config
import jwt

def passwordEncrypt(password):
    return password

def getJWTToken(user):
    algorithm = config.get('ALGORITHM')
    secret_key = config.get('SECRET_KEY')

    user = user.asJSON()
    user.pop('password')

    encoded_jwt = jwt.encode(user, secret_key, algorithm=algorithm)
    return encoded_jwt.decode('utf8')

def retriveJWTInformation(token):
    algorithm = config.get('ALGORITHM')
    secret_key = config.get('SECRET_KEY')
    encoded_jwt = token.encode('utf8')
    
    user = jwt.decode(encoded_jwt, secret_key, algorithms=[algorithm])
    return user