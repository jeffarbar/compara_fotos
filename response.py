class Response:

    def __init__(self, code, message, diretorio_uuid=None):
        self.code = code
        if message:
            self.message = str(message)

        self.diretorio_uuid = diretorio_uuid