from bs4 import BeautifulSoup
from requests import Session

from wristlock import KEVO_START_URL, KEVO_LOGIN_URL
from wristlock.exceptions import NotFoundError, UnauthorizedError


class BaseRun(object):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.result_page = None
        self.session = Session()

    def run(self):
        token = self._get_token()
        login_payload = {
            "user[username]": self.email,
            "user[password]": self.password,
            "authenticity_token": token
        }
        result = self.session.post(KEVO_LOGIN_URL, login_payload)
        try:
            result.raise_for_status()
        except:
            raise UnauthorizedError()
        self.result_page = result.text

    def _get_token(self) -> str:
        token = None
        result = self.session.get(KEVO_START_URL)
        login_page = BeautifulSoup(result.text, "html.parser")
        for field in login_page.find_all("input"):
            if field.get("name") == "authenticity_token":
                token = field.get("value")
                break
        if not token:
            raise NotFoundError("Could not find auth token on signin page")
        return token

