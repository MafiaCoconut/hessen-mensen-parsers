from datetime import datetime, timedelta

from icecream import ic

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.canteen_service import CanteensService
from application.use_cases.set_jobs_by_canteen_use_case import SetJobsByCanteenUseCase
from application.use_cases.set_s3_scheduler_job import SetS3JobUseCase
from domain.entities.job import Job
from infrastructure.config.logs_config import log_decorator


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 set_canteens_jobs_use_case: SetJobsByCanteenUseCase,
                 set_s3_jobs_use_case: SetS3JobUseCase,
                 canteens_service: CanteensService,
                 ):
        self.canteens_service = canteens_service
        self.scheduler_interface = scheduler_interface
        self.set_canteens_jobs_use_case = set_canteens_jobs_use_case
        self.set_s3_jobs_use_case = set_s3_jobs_use_case

    @log_decorator()
    async def execute(self):
        await self.set_parser_marburg_erlenring()
        await self.set_parser_marburg_lahnberge()
        await self.set_parser_marburg_bistro()
        await self.set_parser_marburg_cafeteria()
        await self.set_parser_marburg_mo_diner()
        await self.set_parser_giessen_thm()

        await self.set_s3_upload_logs()
        await self.scheduler_interface.start()

    @log_decorator()
    async def set_parser_marburg_erlenring(self):
        await self.set_canteens_jobs_use_case.execute(
            canteen=await self.canteens_service.get_canteen_obj(canteen_id=1),
            func=self.canteens_service.parse_canteen
        )

    @log_decorator()
    async def set_parser_marburg_lahnberge(self):
        await self.set_canteens_jobs_use_case.execute(
            canteen=await self.canteens_service.get_canteen_obj(canteen_id=2),
            func=self.canteens_service.parse_canteen
        )

    @log_decorator()
    async def set_parser_marburg_cafeteria(self):
        await self.set_canteens_jobs_use_case.execute(
            canteen=await self.canteens_service.get_canteen_obj(canteen_id=3),
            func=self.canteens_service.parse_canteen
        )

    @log_decorator()
    async def set_parser_marburg_mo_diner(self):
        await self.set_canteens_jobs_use_case.execute(
            canteen=await self.canteens_service.get_canteen_obj(canteen_id=4),
            func=self.canteens_service.parse_canteen
        )

    @log_decorator()
    async def set_parser_marburg_bistro(self):
        await self.set_canteens_jobs_use_case.execute(
            canteen=await self.canteens_service.get_canteen_obj(canteen_id=5),
            func=self.canteens_service.parse_canteen
        )

    @log_decorator()
    async def set_parser_giessen_thm(self):
        await self.set_canteens_jobs_use_case.execute(
            canteen=await self.canteens_service.get_canteen_obj(canteen_id=6),
            func=self.canteens_service.parse_canteen
        )

    @log_decorator()
    async def set_s3_upload_logs(self):
        await self.set_s3_jobs_use_case.execute()