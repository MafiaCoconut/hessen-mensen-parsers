from src.app.application.interfaces.parser_interface import CanteenParserInterface


class ParseMensaUseCase:
    def __init__(self, parser_interface: CanteenParserInterface):
        self.parser_interface = parser_interface

    def execute(self):
        return self.parser_interface.parse()

