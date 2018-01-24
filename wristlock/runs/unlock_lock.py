from wristlock.entities import LockState
from wristlock.runs import BaseCommandRun


class UnlockLock(BaseCommandRun):
    def __init__(self, email: str, password: str, lock_id: str):
        super(UnlockLock, self).__init__(email=email, password=password, lock_id=lock_id)

    def run(self):
        super(UnlockLock, self).run()
        return self._unlock()

    def _unlock(self):
        self.session.get(self.unlock_command_url)
        return self.wait_for_state(state=LockState.UNLOCKED)
