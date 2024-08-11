from application.interfaces.scheduler_interface import SchedulerInterface
from domain.entities.canteen import Canteen
from domain.entities.job import Job


class SetJobsByCanteenUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface
                 ):
        self.scheduler_interface = scheduler_interface

    async def execute(self, canteen: Canteen, func):
        if canteen.status == "active":
            try:
                times: dict = canteen.times
                times_keys = list(times.keys())
                for i in range(len(times_keys)):
                    await self.scheduler_interface.add_job(
                        Job(
                            func=func,
                            trigger='cron',
                            id=f"parser_{canteen.canteen_id}_{times_keys[i]}",
                            hour=times.get(times_keys[i]).get('hour'),
                            minute=times.get(times_keys[i]).get('minute'),
                            day_of_week='mon-fri',
                            args=[canteen.canteen_id]
                        )
                    )
            except Exception as e:
                print(f"Error setting jobs for canteen {canteen.canteen_id}: {e}")


