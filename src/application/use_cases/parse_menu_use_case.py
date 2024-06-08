from application.interfaces.parser_interface import CanteenParserInterface


class ParseCanteensMenuUseCase:
    def __init__(self, parser_interface: CanteenParserInterface):
        self.parser_interface = parser_interface

    def execute(self):
        return self.parser_interface.parse()

