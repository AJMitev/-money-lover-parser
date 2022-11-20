import uuid
from datetime import date


class Category:
    def __init__(self, name, type, id=uuid.uuid4()):
        self.id = id
        self.name = name
        self.type = type
        self.created_on = date.today().strftime("%d/%m/%Y")
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
