from datetime import datetime, timedelta

from application.interfaces.scheduler_interface import SchedulerInterface


# from application.services.scheduler_service import SchedulerService
# from application.repositories.meeting_repository import MeetingRepository
# from application.repositories.scheduler_repository import SchedulerRepository


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 ):

        self.scheduler_interface = scheduler_interface

    async def execute(self):
        await self.scheduler_interface.set_all_jobs()
