import json
import time

from wristlock import KEVO_COMMANDS_URL_BASE
from wristlock.entities import LockState
from wristlock.exceptions import TimeoutError
from wristlock.runs import BaseRun


class BaseCommandRun(BaseRun):
    def __init__(self, email: str, password: str, lock_id: str):
        super(BaseCommandRun, self).__init__(email=email, password=password)
        self.lock_id = lock_id

    def run(self):
        super(BaseCommandRun, self).run()

    def wait_for_state(self, state: LockState, timeout: int=20):
        start_time = time.time()
        while True:
            time.sleep(1)
            lock_state = self.refresh_lock_state()
            if lock_state == state:
                print('returning')
                return lock_state
            if time.time() - start_time > timeout:
                raise TimeoutError()

    def refresh_lock_state(self):
        command_url = KEVO_COMMANDS_URL_BASE + "/lock.json?arguments={}".format(self.lock_id)
        res = self.session.get(command_url)
        res.raise_for_status()
        data = json.loads(res.text)
        return data["bolt_state"].lower()

    @property
    def lock_command_url(self):
        return KEVO_COMMANDS_URL_BASE + "/remote_lock.json?arguments={}".format(self.lock_id)

    @property
    def unlock_command_url(self):
        return KEVO_COMMANDS_URL_BASE + "/remote_unlock.json?arguments={}".format(self.lock_id)
