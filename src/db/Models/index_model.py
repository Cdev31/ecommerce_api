from pymongo.errors import CollectionInvalid
from pymongo.database import Database

#internal imports
from db.Models.product_model import product_schema


class Model:
    def __init__(self,db:Database,collection_name:str,schema:dict):
        try:
            db.create_collection(collection_name,validator=schema)
        except CollectionInvalid:
            pass


def collection_add(db:Database)-> None:
        Model(db=db,collection_name='Users',schema={}),
        Model(db=db,collection_name='Categories',schema={}),
        Model(db=db,collection_name='Products',schema=product_schema),
        Model(db=db,collection_name='Orders',schema={})    