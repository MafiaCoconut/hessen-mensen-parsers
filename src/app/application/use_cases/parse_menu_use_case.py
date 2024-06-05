class ParseMensaUseCase:
    def __init__(self, parser_service):
        self.parser_service = parser_service

    def execute(self, canteen_name: str):
        return self.parser_service.parse(canteen_name)

