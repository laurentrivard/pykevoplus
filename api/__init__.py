from flask import Blueprint, Response
from flask_restful import Api
from json import dumps

from wristlock.exceptions import KevoError


wristlock_http_bp = Blueprint('wristlock_http_bp', __name__)

http_api = Api(wristlock_http_bp)


def build_error_response(status_code, message):
    error_dict = {"statusCode": status_code, "message": message}
    response = Response(dumps(error_dict))
    response.status_code = status_code
    response.headers['Content-Type'] = 'application/json'
    return response


@wristlock_http_bp.errorhandler(KevoError)
def handle_exception(error):
    return build_error_response(error.status_code, error.message)


@wristlock_http_bp.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response


from api.views import auth_views, lock_views

