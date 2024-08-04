from enum import Enum


class ErrorCodes(Enum):
    DATA_IS_WRONG = 'Canteen have wrong data'
    NOT_FOUND = 'Canteen not found'


class CanteenException(Exception):
    """Базовый класс для исключений, связанных с Canteen."""
    pass


class CanteenWrongDataException(CanteenException):
    def __init__(self, message=ErrorCodes.DATA_IS_WRONG.value):
        self.message = message
        super().__init__(self.message)


class CanteenNotFoundException(CanteenException):
    def __init__(self, message=ErrorCodes.NOT_FOUND.value):
        self.message = message
        super().__init__(self.message)