from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from flask_jwt_extended import create_access_token, jwt_required, \
    get_jwt_identity, set_access_cookies

from lamapi import db
from lamapi.models.user import User
from lamapi.auth import passwordEncrypt

from sqlalchemy.exc import IntegrityError

import json

put_user_parser = RequestParser()
put_user_parser.add_argument('login', help = 'Este campo é obrigatório', required = True)
put_user_parser.add_argument('password', help = 'Este campo é obrigatório', required = True)
put_user_parser.add_argument('email', help = 'Este campo é obrigatório', required = True)

post_user_parser = RequestParser()
post_user_parser.add_argument('login', help = 'Este campo é obrigatório', required = True)
post_user_parser.add_argument('password', help = 'Este campo é obrigatório', required = True)

class AuthController(Resource):
    """TO-DO: Must create documentation here"""

    # ---- TO-DO: Post Auth
    def post(self):
        """TO-DO: Must create documentation here"""

        data = post_user_parser.parse_args()
        
        login = data['login']
        password = passwordEncrypt(data['password'])

        user = User.query.filter_by(login=login, password=password).first()

        if not user:
            return { 'msg': 'Login e/ou Senha não estão corretos.' }, 401
        
        response_data = { 'msg': 'Login was done.', 'login': user.login, 'email': user.email }
        access_token = create_access_token(identity=user.login, headers={ 'email' : user.email })
        response = make_response(json.dumps(response_data))
        set_access_cookies(response, access_token)
        return response

    # ---- TO-DO: Register a New User
    def put(self):
        """TO-DO: Must create documentation here"""

        data = put_user_parser.parse_args()

        login = data['login']
        password = passwordEncrypt(data['password'])
        email = data['email']

        new_user = User(login=login, password=password, email=email)
        try:
            new_user.saveToDB()
        except IntegrityError:
            return { 'msg': f'Login {login} ou/e Email {email} ja está sendo usado.'}, 200
        except:
            return { 'msg': 'Um erro aconteceu' }, 500
        return { 'msg': f'User {login} was created' }



