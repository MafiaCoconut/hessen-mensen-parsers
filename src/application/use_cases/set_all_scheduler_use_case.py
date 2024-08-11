from datetime import datetime, timedelta

from icecream import ic

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.canteen_service import CanteensService
from domain.entities.job import Job


# from application.services.scheduler_service import SchedulerService
# from application.repositories.meeting_repository import MeetingRepository
# from application.repositories.scheduler_repository import SchedulerRepository


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 canteens_service: CanteensService,

                 ):
        self.scheduler_interface = scheduler_interface
        self.canteens_service = canteens_service

    async def execute(self):
        await self.set_parser_marburg_erlenring()
        await self.set_parser_marburg_lahnberge()
        await self.set_parser_marburg_bistro()
        await self.set_parser_marburg_cafeteria()
        await self.set_parser_marburg_mo_diner()
        await self.set_parser_giessen_thm()

        await self.scheduler_interface.start()

    async def template_set_canteens_times(self, canteen_id: int):
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

    async def set_parser_marburg_erlenring(self):
        await self.template_set_canteens_times(canteen_id=1)

    async def set_parser_marburg_lahnberge(self):
        await self.template_set_canteens_times(canteen_id=2)

    async def set_parser_marburg_cafeteria(self):
        await self.template_set_canteens_times(canteen_id=3)

    async def set_parser_marburg_mo_diner(self):
        await self.template_set_canteens_times(canteen_id=4)

    async def set_parser_marburg_bistro(self):
        await self.template_set_canteens_times(canteen_id=5)

    async def set_parser_giessen_thm(self):
        await self.template_set_canteens_times(canteen_id=6)

