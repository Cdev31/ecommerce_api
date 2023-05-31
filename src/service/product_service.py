from bson import ObjectId
from Interfaces.product_interface import InterfaceProduct

from db.client import db

class Service(InterfaceProduct):

    def find_products(self):
        return {}

    def find_one_product(self, id: str):
        db['Products'].find_one({'_id': ObjectId(id)})
        return {}
    
    def create_product(self, body: dict):
        return {}
    
    def update_info_product(self, id: str, chages: dict):
        return {}
    
    def delete_product(self, id: str):
        return {}