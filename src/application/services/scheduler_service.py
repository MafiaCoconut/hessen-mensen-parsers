# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
from domain.entities.job import Job


class SchedulerService:
    def __init__(self, scheduler: SchedulerInterface):
        self.scheduler = scheduler
        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase()

    async def add_job(self, job: Job) -> None:
        await self.scheduler.add_job(job)

    async def add_all_jobs(self, jobs: list) -> None:
        for job in jobs:
            await self.scheduler.add_job(job)
                # func=job.func,
                # trigger=job.trigger,
                # run_date=job.run_date,
                # args=job.args
            # )

    async def delete_job(self, job_id: str) -> None:
        await self.scheduler.delete_job(job_id)
