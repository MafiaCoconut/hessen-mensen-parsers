from application.interfaces.scheduler_interface import SchedulerInterface
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase


class StartSchedulersService:
    def __init__(self, scheduler_interface: SchedulerInterface):
        self.scheduler_interface = scheduler_interface

        self.scheduler_use_case = SetAllSchedulersJobsUseCase(
            scheduler_interface=scheduler_interface
        )

    def execute(self):
        self.scheduler_use_case.execute()

