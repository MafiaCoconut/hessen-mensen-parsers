from infrastructure.config.canteens_interfaces_provider import giessen_cafeteria_campus_tor
from infrastructure.providers_impl.canteens_provider_impl import CanteensDependencyProviderImpl
from infrastructure.config import canteens_interfaces_provider
from infrastructure.providers_impl.repositories_provider_impl import RepositoriesProviderImpl

canteens_provider = CanteensDependencyProviderImpl(
    marburg_erlenring=canteens_interfaces_provider.marburg_erlenring,
    marburg_lahnberge=canteens_interfaces_provider.marburg_lahnberge,
    marburg_bistro=canteens_interfaces_provider.marburg_bistro,
    marburg_cafeteria=canteens_interfaces_provider.marburg_cafeteria,
    marburg_mo_diner=canteens_interfaces_provider.marburg_mo_diner,
    giessen_thm=canteens_interfaces_provider.giessen_thm,
    giessen_cafeteria_campus_tor=giessen_cafeteria_campus_tor,
)

repositories_provider = RepositoriesProviderImpl()
