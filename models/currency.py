import uuid


class Currency:
    def __init__(self, symbol, id=uuid.uuid4()):
        self.id = id
        self.symbol = symbol
