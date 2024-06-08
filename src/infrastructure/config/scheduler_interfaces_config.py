from infrastructure.interfaces_impl.scheduler_interface_impl import SchedulerInterfaceImpl
from infrastructure.config.canteen_service_config import canteens_service


scheduler_interface = SchedulerInterfaceImpl(
    canteen_service=canteens_service
)
