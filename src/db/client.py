from pymongo import MongoClient

#intenal imports
from config.config import config
from db.Models.index_model import collection_add

client:MongoClient = MongoClient(config['db_url'])

db = client['ecomerce_db']
collection_add(db)
