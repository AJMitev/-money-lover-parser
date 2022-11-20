from money_lover_export_parser import parse_xlsx
import os
import shutil
from functools import reduce
from repositories import categories
from repositories import currencies
from repositories import transactions


def insert_transactions(collection):
    for category in collection:
        if categories.exists(category.name) == False:
            categories.inset(category)

        for transaction in category.transactions:
            transaction_currency = currencies.find(transaction.currency)
            transactions.insert(transaction, category.id,
                                transaction_currency.id)


def upsert_currencies(collection):
    for currency in collection:
        if currencies.exists(currency.symbol) == False:
            currencies.insert(currency)


root = os.path.dirname(__file__)
inputs = f'{root}/data/input/'
output = f'{root}/data/proccessed'

for file in os.listdir(inputs):
    filename = os.path.join(inputs, file)

    parsed_result = parse_xlsx.parse_report(filename)

    upsert_currencies(parsed_result["currencies"])
    insert_transactions(parsed_result["categories"])

    shutil.move(filename, output)
