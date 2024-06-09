from typing import List

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.canteen_service import CanteenService
from domain.entities.job import Job
from infrastructure.config.scheduler_config import scheduler

class SchedulerInterfaceImpl(SchedulerInterface):
    def __init__(self, canteen_service: CanteenService):
        self.canteen_service = canteen_service

    @staticmethod
    def add_job(job: Job) -> None:
        scheduler.add_job(
            func=job.func,
            trigger=job.trigger,
            run_date=job.run_date,
            args=job.args
        )

    def set_all_jobs(self):
        self.set_canteens_parsers()

    def set_canteens_parsers(self):
        self.set_parser_marburg_erlenring()
        self.set_parser_marburg_lahnberge()
        self.set_parser_marburg_bistro()
        self.set_parser_marburg_cafeteria()
        self.set_parser_marburg_mo_diner()
        self.set_parser_giessen_thm()
        scheduler.start()


    def set_parser_marburg_erlenring(self):
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mensa_erlenring_1",
                          hour=11, minute=0,
                          day_of_week='mon-fri',
                          args=[1])

        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mensa_erlenring_2",
                          hour=11, minute=30,
                          day_of_week='mon-fri',
                          args=[1])

        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mensa_erlenring_3",
                          hour=11, minute=43,
                          day_of_week='mon-fri',
                          args=[1])

        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mensa_erlenring_4",
                          hour=21, minute=22,
                          # day_of_week='mon-fri',
                          args=[1])

    def set_parser_marburg_lahnberge(self):
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mensa_lahnberge_1",
                          hour=11, minute=0,
                          day_of_week='mon-fri',
                          args=[2])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mensa_lahnberge_2",
                          hour=11, minute=30,
                          day_of_week='mon-fri',
                          args=[2])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mensa_lahnberge_3",
                          hour=11, minute=40,
                          day_of_week='mon-fri',
                          args=[2])

    def set_parser_marburg_bistro(self):
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_bistro_1",
                          hour=9, minute=0,
                          day_of_week='mon-fri',
                          args=[3])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_bistro_2",
                          hour=10, minute=30,
                          day_of_week='mon-fri',
                          args=[3])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_bistro_3",
                          hour=11, minute=35,
                          day_of_week='mon-fri',
                          args=[3])


    def set_parser_marburg_cafeteria(self):
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_cafeteria_lahnberge_1",
                          hour=8, minute=0,
                          day_of_week='mon-fri',
                          args=[4])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_cafeteria_lahnberge_2",
                          hour=10, minute=0,
                          day_of_week='mon-fri',
                          args=[4])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_cafeteria_lahnberge_3",
                          hour=12, minute=0,
                          day_of_week='mon-fri',
                          args=[4])

    def set_parser_marburg_mo_diner(self):
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mo_diner_1",
                          hour=9, minute=0,
                          day_of_week='mon-fri',
                          args=[5])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mo_diner_2",
                          hour=10, minute=0,
                          day_of_week='mon-fri',
                          args=[5])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_mo_diner_3",
                          hour=11, minute=0,
                          day_of_week='mon-fri',
                          args=[5])

    def set_parser_giessen_thm(self):
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_thm_1",
                          hour=11, minute=0,
                          day_of_week='mon-fri',
                          args=[6])
        scheduler.add_job(self.canteen_service.parse_canteen,
                          trigger='cron',
                          id="parser_thm_2",
                          hour=11, minute=40,
                          day_of_week='mon-fri',
                          args=[6])
        # scheduler.add_job(self.canteen_service.parse_canteen,
        #                   trigger='cron',
        #                   id="parser_thm_3",
        #                   hour=8, minute=7,
        #                   day_of_week='mon-fri',
        #                   args=[6])