import psycopg2
import psycopg2.extras
from configuration import config


def execute(query, values):
    cfg = config.get_db_config()
    conn = psycopg2.connect(host=cfg["Host"], database=cfg["Database"],
                            user=cfg["User"], password=cfg["Password"])
    psycopg2.extras.register_uuid()

    cur = conn.cursor()

    cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()


def get_all(query):
    cfg = config.get_db_config()
    conn = psycopg2.connect(host=cfg["Host"], database=cfg["Database"],
                            user=cfg["User"], password=cfg["Password"])

    cur = conn.cursor()

    cur.execute(query)

    records = cur.fetchall()

    cur.close()
    conn.close()

    return records


def get_one(query):
    cfg = config.get_db_config()
    conn = psycopg2.connect(host=cfg["Host"], database=cfg["Database"],
                            user=cfg["User"], password=cfg["Password"])

    cur = conn.cursor()

    cur.execute(query)

    records = cur.fetchone()

    cur.close()
    conn.close()

    return records
