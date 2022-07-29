class Response:

    def __init__(self, code, message):
        self.code = code
        if message:
            self.message = str(message)
