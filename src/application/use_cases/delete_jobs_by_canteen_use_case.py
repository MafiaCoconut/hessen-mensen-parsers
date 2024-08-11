from application.services.scheduler_service import SchedulerService


class DeleteJobsByCanteenUseCase:
    def __init__(self,
                 scheduler_service: SchedulerService,
                 ):
        self.scheduler_service = scheduler_service