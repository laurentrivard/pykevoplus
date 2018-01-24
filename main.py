from api.app_factory import create_app


app, socketio = create_app()
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=80, debug=True)
