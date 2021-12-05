import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv();

_password = os.getenv("DB_PASSWORD")
_username = os.getenv("DB_USERNAME")

_uri = f'mongodb+srv://{_username}:{_password}@hwatudatacollection1.umf8y.mongodb.net'

db= MongoClient(_uri)['hwatugame']['results']
