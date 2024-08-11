from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.canteen_service import CanteensService
from domain.entities.job import Job


class SetJobsByCanteenUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 canteens_service: CanteensService,
                 ):
        self.scheduler_interface = scheduler_interface
        self.canteens_service = canteens_service

    async def execute(self, canteen_id: int):
        canteen = await self.canteens_service.get_canteen_obj(canteen_id=canteen_id)
        times: dict = canteen.times
        times_keys = list(times.keys())
        for i in range(len(canteen.times)):
            await self.scheduler_interface.add_job(
                Job(
                    func=self.canteens_service.parse_canteen,
                    trigger='cron',
                    id=f"parser_{canteen_id}_{times_keys[i]}",
                    hour=times.get(times_keys[i]).get('hour'),
                    minute=times.get(times_keys[i]).get('minute'),
                    day_of_week='mon-fri',
                    args=[canteen_id]
                )
            )

