from bson import ObjectId
from pymongo import ReturnDocument
from bson.errors import InvalidId
#internal imports
from Interfaces.product_interface import InterfaceProduct
from db.client import db

class Service(InterfaceProduct):

    def find_products(self):
        list_product = []
        products = db['Products'].find()
        for e in products:
            e['id'] = str(e['_id'])
            del e['_id']
            list_product.append(e)
        return list_product

    def find_one_product(self, id: str):
        try: 
            product =  db['Products'].find_one({'_id': ObjectId(id)})
            if product == None:
                return None
            product['id'] = str(product['_id'])
            del product['_id']
            return product
        except InvalidId as err :
            return err
        
    
    def create_product(self, body: dict):
        id = db['Products'].insert_one(body)
        newProduct = self.find_one_product(id.inserted_id)
        return newProduct
    
    def update_info_product(self, id: str, changes: dict):
        try:
            product = db['Products'].find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set':changes},return_document=ReturnDocument.AFTER)

            updateProduct = self.find_one_product(product['_id'])
            return updateProduct
        except InvalidId as err:
            return err
      
    def delete_product(self, id: str):
        try:
            deleted = db['Products'].delete_one({'_id': ObjectId(id)})
            return deleted.deleted_count
        except InvalidId as err:
            return err