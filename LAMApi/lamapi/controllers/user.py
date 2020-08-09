from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from lamapi import db
from lamapi.models.user import UserModel
from sqlalchemy.exc import IntegrityError


put_user_parser = RequestParser()
put_user_parser.add_argument('login', help = 'Este campo é obrigatório', required = True)
put_user_parser.add_argument('password', help = 'Este campo é obrigatório', required = True)
put_user_parser.add_argument('email', help = 'Este campo é obrigatório', required = True)



class UserController(Resource):

    # ---- TO-DO: Get Music
    def get(self):
        return 'In progress...'

    # ---- TO-DO: Register a New User
    def put(self):
        data = put_user_parser.parse_args()

        login = data['login']
        password = data['password']
        email = data['email']

        new_user = UserModel(login=login,password=password,email=email)
        try:
            new_user.save_to_db()
        except IntegrityError:
            return { 'message': f'Login {login} ja está sendo usado.' }, 500
        except:
            return { 'message': 'Um erro aconteceu' }, 500

        return { 'message': f'User {login} was created' }
