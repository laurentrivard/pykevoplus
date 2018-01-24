from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


def create_app(**config_overrides):

    # apply config overrides passed in as a dependency
    app.config.from_object('api.config')
    app.config.update(config_overrides)

    from api import wristlock_http_bp as http
    app.register_blueprint(http, url_prefix='/v1')
    return app, socketio
