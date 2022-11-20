from database import db
from models.category import Category
from models.category_type import CategoryType


def get_all():
    records = db.get_all("SELECT id, name, type FROM my_data")
    entities = {}
    for record in records:
        id = record[0]
        name = record[1]
        type = CategoryType(record[2])

        category = Category(name, type, id)
        entities.update(category)
    return records


def inset(category):
    query = f"INSERT INTO categories (id, name, type) VALUES (%s, %s, %s)"
    db.execute(query, [category.id, category.name, category.type.value])


def exists(name):
    query = f"SELECT * FROM categories WHERE name = '{name}';"
    result = db.get_all(query)
    return len(result) > 0
