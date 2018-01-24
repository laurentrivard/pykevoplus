from typing import List
import json

from bs4 import BeautifulSoup

from wristlock import KEVO_COMMANDS_URL_BASE
from wristlock.entities import Lock
from wristlock.runs import BaseRun


class GetLocks(BaseRun):
    def __init__(self, email: str, password: str):
        super(GetLocks, self).__init__(email=email, password=password)

    def run(self) -> List[Lock]:
        # TODO: Keep result page in mem?
        super(GetLocks, self).run()
        lock_page = BeautifulSoup(self.result_page, "html.parser")
        return self._get_locks(lock_page=lock_page)

    def _get_locks(self, lock_page: str) -> List[Lock]:
        locks = list()
        for lock in lock_page.find_all("ul", "lock"):
            lock_info = lock.find("div", class_="lock_unlock_container")
            lock_id = lock_info.get("data-lock-id")
            lock_detail_url = KEVO_COMMANDS_URL_BASE + "/lock.json?arguments={}".format(lock_id)
            detail_result = self.session.get(lock_detail_url)
            lock_details = json.loads(detail_result.text)
            locks.append(Lock.from_json(lock_details))
        return locks
