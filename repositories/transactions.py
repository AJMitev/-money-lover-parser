from database import db


def insert(transaction, category_id, currency_id):
    query = f"INSERT INTO transactions VALUES (%s, %s, %s, %s, %s, %s)"
    db.execute(query, [transaction.id, transaction.amount, transaction.date,
               currency_id, transaction.description, category_id])
