class KevoError(Exception):
    """Base exception for all Kevo errors"""
    status_code = 400

    def __init__(self, message=None, *args, **kwargs):
        super(KevoError, self).__init__(*args, **kwargs)
        self.message = message


class NotFoundError(Exception):
    status_code = 404
    message = "Lock not found"


class TimeoutError(Exception):
    status_code = 400
    message = "Timeout error"
