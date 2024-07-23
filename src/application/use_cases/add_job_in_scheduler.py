from application.scheduler.interfaces.scheduler_interface import SchedulerInterface
from domain.entities.job import Job


class AddJobInSchedulerUseCase:
    def __init__(self, scheduler_interface: SchedulerInterface):
        self.scheduler_interface = scheduler_interface

    async def execute(self, job: Job):
        await self.scheduler_interface.add_job(job=job)

