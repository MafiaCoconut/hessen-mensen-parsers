from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class SchedulerInterface(ABC):
    @abstractmethod
    def add_job(self, job) -> None:
        pass

    @abstractmethod
    def set_all_jobs(self) -> List:
        pass


