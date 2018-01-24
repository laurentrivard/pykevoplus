from wristlock.runs import BaseCommandRun

from wristlock.entities import LockState


class LockLock(BaseCommandRun):
    def __init__(self, email: str, password: str, lock_id: str):
        super(LockLock, self).__init__(email=email, password=password, lock_id=lock_id)

    def run(self):
        super(LockLock, self).run()
        self._lock()

    def _lock(self):
        print('--------------------------doing lock')
        self.session.get(self.lock_command_url)
        self.wait_for_state(state=LockState.LOCKED)
