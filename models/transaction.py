import uuid
from datetime import datetime


class Transaction:
    def __init__(self, amount, currency, date, description, id=uuid.uuid4()):
        self.id = id
        self.amount = amount
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.description = description
        self.currency = currency
