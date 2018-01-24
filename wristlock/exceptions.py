class KevoError(Exception):
    """Base exception for all Kevo errors"""
    status_code = 400

    def __init__(self, message=None, *args, **kwargs):
        super(KevoError, self).__init__(*args, **kwargs)
        self.message = message


class NotFoundError(KevoError):
    status_code = 404
    message = "Lock not found"


class TimeoutError(KevoError):
    status_code = 400
    message = "Timeout error"


class UnauthorizedError(KevoError):
    status_code = 401
    message = "Unauthorized"
