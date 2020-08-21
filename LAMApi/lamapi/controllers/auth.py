from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from lamapi import db
from lamapi.models.user import UserModel
from lamapi.auth import passwordEncrypt, getJWTToken
from sqlalchemy.exc import IntegrityError


put_user_parser = RequestParser()
put_user_parser.add_argument('login', help = 'Este campo é obrigatório', required = True)
put_user_parser.add_argument('password', help = 'Este campo é obrigatório', required = True)
put_user_parser.add_argument('email', help = 'Este campo é obrigatório', required = True)



post_user_parser = RequestParser()
post_user_parser.add_argument('login', help = 'Este campo é obrigatório', required = True)
post_user_parser.add_argument('password', help = 'Este campo é obrigatório', required = True)



class AuthController(Resource):

    # ---- TO-DO: Post Auth
    def post(self):
        data = post_user_parser.parse_args()

        login = data['login']
        password = passwordEncrypt(data['password'])

        user = UserModel.query.filter_by(login=login, password=password).first()

        if user:
            return {
                'login' : user.login,
                'email' : user.email,
                'accessToken' : getJWTToken(user)
            }
        return { 'message': 'Login e/ou Senha não estão corretos.' }, 500

    # ---- TO-DO: Register a New User
    def put(self):
        data = put_user_parser.parse_args()

        login = data['login']
        password = passwordEncrypt(data['password'])
        email = data['email']

        new_user = UserModel(login=login, password=password, email=email)
        try:
            new_user.saveToDB()
        except IntegrityError:
            return { 'message': f'Login {login} ou/e Email {email} ja está sendo usado.'}, 500
        except:
            return { 'message': 'Um erro aconteceu' }, 500
        return { 'message': f'User {login} was created' }



