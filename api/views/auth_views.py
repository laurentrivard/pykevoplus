from flask import request
from flask_restful import Resource

from api import http_api
from wristlock.exceptions import KevoError
from wristlock.runs import Login


class LoginView(Resource):
    """ Simple view that'll thrown an exception if
    the user isn't able to log in
    """
    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']
            Login(email=email,
                  password=password).run()
        except KeyError as key:
            raise KevoError("Bad request. Missing key '{}'".format(key))


http_api.add_resource(LoginView, '/login')
