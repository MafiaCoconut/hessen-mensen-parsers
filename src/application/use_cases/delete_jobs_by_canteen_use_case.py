from application.interfaces.scheduler_interface import SchedulerInterface
from domain.entities.canteen import Canteen


class DeleteJobsByCanteenUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 ):
        self.scheduler_interface = scheduler_interface

    async def execute(self, canteen: Canteen):
        times: dict = canteen.times
        times_keys = list(times.keys())

        for i in range(len(times_keys)):
            print(f"parser_{canteen.canteen_id}_{times_keys[i]}")
            await self.scheduler_interface.remove(job_id=f"parser_{canteen.canteen_id}_{times_keys[i]}")



