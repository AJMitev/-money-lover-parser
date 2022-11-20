import configparser
import os


def get_db_config():
    config = configparser.ConfigParser()
    config.read(
        config.read(os.path.join(os.path.dirname(__file__), 'config.ini')))
    database = config['DATABASE']
    return database
