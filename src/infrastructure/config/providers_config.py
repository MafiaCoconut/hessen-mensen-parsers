from infrastructure.providers_impl.canteens_provider_impl import CanteensDependencyProviderImpl
from infrastructure.config import interfaces_provider

canteens_provider = CanteensDependencyProviderImpl(
    marburg_erlenring=interfaces_provider.marburg_erlenring,
    marburg_lahnberge=interfaces_provider.marburg_lahnberge,
    marburg_bistro=interfaces_provider.marburg_bistro,
    marburg_cafeteria=interfaces_provider.marburg_cafeteria,
    marburg_mo_diner=interfaces_provider.marburg_mo_diner,
    giessen_thm=interfaces_provider.marburg_mo_diner,
)

