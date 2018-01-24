from . import BaseRun


class Login(BaseRun):
    """
    This class only runs the Login steps in BaseRun
    """
    def __init__(self, email: str, password: str):
        super(Login, self).__init__(email=email, password=password)

    def run(self):
        super(Login, self).run()
