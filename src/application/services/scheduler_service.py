# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.canteen_service import CanteensService
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
from application.use_cases.set_jobs_by_canteen_use_case import SetJobsByCanteenUseCase
from domain.entities.job import Job


class SchedulerService:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 canteens_service: CanteensService,
                 ):
        self.scheduler_interface = scheduler_interface
        self.set_jobs_use_case = SetJobsByCanteenUseCase(
            scheduler_interface=scheduler_interface,
            # canteens_service=canteens_service
        )
        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase(
            scheduler_interface=scheduler_interface,
            set_jobs_use_case=self.set_jobs_use_case,
            canteens_service=canteens_service
        )

    async def add_job(self, job: Job) -> None:
        await self.scheduler_interface.add_job(job)

    async def add_all_jobs(self, jobs: list) -> None:
        for job in jobs:
            await self.scheduler_interface.add_job(job)

    async def delete_job(self, job_id: str) -> None:
        await self.scheduler_interface.remove(job_id)

    async def set_start_jobs(self) -> None:
        await self.set_all_schedulers_jobs.execute()
