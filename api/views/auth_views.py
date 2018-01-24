from flask import request
from flask_restful import Resource

from api import api


class LoginView(Resource):

    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']
            print('calling login')
            # Login(email=email,
            #       password=password).run()
        except KeyError:
            raise Exception()  # TODO:


api.add_resource(LoginView, '/login')
