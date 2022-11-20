from database import db
from models.currency import Currency


def insert(currency):
    query = f"INSERT INTO currencies (id, symbol) VALUES (%s, %s);"
    db.execute(query, [currency.id, currency.symbol])


def exists(symbol):
    query = f"SELECT * FROM currencies WHERE symbol='{symbol}';"
    results = db.get_all(query)
    return len(results) > 0


def find(symbol):
    query = f"SELECT * FROM currencies WHERE symbol='{symbol}';"
    cols = db.get_one(query)
    result = Currency(cols[1], cols[0])
    return result
