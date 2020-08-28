from useless.globals import color_codes

class Message:
    def __init__(self, message: str):
        self.message = message
        self.printMessage()

    def printMessage(self):
        print(self.message)

class SuccessMessage(Message):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def printMessage(self):
        print(f'{color_codes["success"]}[+]{self.message}{color_codes["reset"]}')

class WarningMessage(Message):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def printMessage(self):
        print(f'{color_codes["warning"]}[i]{self.message}{color_codes["reset"]}')

class ErrorMessage(Message):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def printMessage(self):
        print(f'{color_codes["error"]}[-]{self.message}{color_codes["reset"]}')