from datetime import datetime, timedelta

from icecream import ic

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.canteen_service import CanteensService
from application.use_cases.set_jobs_by_canteen_use_case import SetJobsByCanteenUseCase
from domain.entities.job import Job


# from application.services.scheduler_service import SchedulerService
# from application.repositories.meeting_repository import MeetingRepository
# from application.repositories.scheduler_repository import SchedulerRepository


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 set_jobs_use_case: SetJobsByCanteenUseCase,
                 ):
        self.scheduler_interface = scheduler_interface
        self.set_jobs_use_case = set_jobs_use_case

    async def execute(self):
        await self.set_parser_marburg_erlenring()
        await self.set_parser_marburg_lahnberge()
        await self.set_parser_marburg_bistro()
        await self.set_parser_marburg_cafeteria()
        await self.set_parser_marburg_mo_diner()
        await self.set_parser_giessen_thm()

        await self.scheduler_interface.start()

    async def set_parser_marburg_erlenring(self):
        await self.set_jobs_use_case.execute(canteen_id=1)

    async def set_parser_marburg_lahnberge(self):
        await self.set_jobs_use_case.execute(canteen_id=2)

    async def set_parser_marburg_cafeteria(self):
        await self.set_jobs_use_case.execute(canteen_id=3)

    async def set_parser_marburg_mo_diner(self):
        await self.set_jobs_use_case.execute(canteen_id=4)

    async def set_parser_marburg_bistro(self):
        await self.set_jobs_use_case.execute(canteen_id=5)

    async def set_parser_giessen_thm(self):
        await self.set_jobs_use_case.execute(canteen_id=6)

