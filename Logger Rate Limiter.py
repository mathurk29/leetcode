class Logger:

    def __init__(self):
        self.ok = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.ok.get(message, 0):
            return False
        self.ok[message] = timestamp + 10
        return True
