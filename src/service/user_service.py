from bson import ObjectId,errors
from pymongo import ReturnDocument
#internal imports
from Interfaces.user_interface import InterfaceUser
from db.client import db

class Service(InterfaceUser):
    def find_users(self):
        users_list = []
        for u in db['Users'].find():
            u['id'] = str(u['_id'])
            del u['_id']
            users_list.append(u)
        return users_list
    

    def find_user(self,id: str):
        try:
            user = db['Users'].find_one({'_id': ObjectId(id)})
            user['id'] = str(user['_id'])
            user['date_of_birth'] = str(user['date_of_birth'])
            del user['_id']     
            return user
        except errors.InvalidId as err:
            return err
    

    def create_user(self, body: dict):
        new_user = db['Users'].insert_one(body)
        response = self.find_user(new_user.inserted_id)
        return response
    
    
    def update_user(self, id: str, changes: dict):
        try: 
            update_user = db['Users'].find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': changes},return_document=ReturnDocument.AFTER)
            reponse = self.find_user(update_user['_id'])
            return reponse
        except errors.InvalidId as err:
            return err
    

    def delete_user(self, id: str):
        try: 
            delete_user = db['Users'].delete_one({'_id':ObjectId(id)})
            return delete_user.deleted_count
        except errors.InvalidId as err:
            return err    