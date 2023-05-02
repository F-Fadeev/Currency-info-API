from pymongo import MongoClient
from config import settings


def get_database():
    client = MongoClient(settings.get_database_url())
    return client[settings.DB_NAME]
