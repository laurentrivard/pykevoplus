import json

from flask import request
from flask_restful import Resource, marshal_with
from flask_socketio import emit
from api.app_factory import socketio

from api import http_api
from api.marshal_fields import lock_fields
from wristlock.exceptions import TimeoutError
from wristlock.runs import GetLocks, LockLock, UnlockLock


class LocksView(Resource):

    @marshal_with(lock_fields)
    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']
            return GetLocks(email=email,
                            password=password).run()
        except KeyError:
            raise Exception()  # TODO:


@socketio.on('lock')
def lock_lock(lock_data: dict):
    try:
        lock_id = lock_data["lockId"]
        email = ''  #  TODO: get from session
        password = ''  # TODO: get from session
        LockLock(email=email, password=password, lock_id=lock_id).run()
    except TimeoutError:
        return 'error'


@socketio.on('unlock')
def unlock_lock(lock_data: dict):
    try:
        lock_id = lock_data["lockId"]
        email = ''  #  TODO: get from session
        password = ''  # TODO: get from session
        response = UnlockLock(email=email, password=password, lock_id=lock_id).run()
        emit(response)
    except TimeoutError:
        return 'error'


@socketio.on('connect')
def connect():
    emit('response', {'data': 'Connected'})


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

http_api.add_resource(LocksView, '/locks')
