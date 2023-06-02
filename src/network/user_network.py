from fastapi import HTTPException
from bson import errors
from starlette import status
import datetime
#imports services
from service.user_service import Service
from Interfaces.response_types import IResponse,StatusMessage
from utils.hash_pass import hash_password

user_service = Service()

class UserNetwork():

    def finds(self):
        response= user_service.find_users()
        return IResponse(
            message='Users Founds',
            response=response,
            status=StatusMessage.SUCCESS
        )
    
    def find_one(self,id:str):
        response = user_service.find_user(id)
        if isinstance(response,errors.InvalidId):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Invalid Id')
        elif response == None:
            return IResponse(
                message=f'User with id: {id} not found',
                response={},
                status=StatusMessage.NOT_SUCCESSFUL
            )
        return IResponse(
            message='User found',
            response=response,
            status=StatusMessage.SUCCESS
        )
    
    def create(self,body:dict):

        body['password'] = hash_password(body['password'])

        body['role'] = str(body['role'])

        body['date_of_birth'] = datetime.datetime(
            year=body['date_of_birth'].year,
            month=body['date_of_birth'].month, 
            day=body['date_of_birth'].day)
        
        del body['confirm_password']

        response = user_service.create_user(body)

        return IResponse(
            message='User Created',
            response=response,
            status=StatusMessage.CREATED
        )
    
    def update(self,id:str,changes:dict):
        response = user_service.update_user(id,changes)
        if isinstance(response,errors.InvalidId):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Invalid Id')
        elif response == None:
            return IResponse(
                message=f'User with id: {id} not found',
                response={},
                status=StatusMessage.NOT_SUCCESSFUL
            )
        return IResponse(
            message='User Updated',
            response=response,
            status=StatusMessage.UPDATED
        )
    


    def delete(self,id:str):
        response = user_service.delete_user(id)
        if isinstance(response,errors.InvalidId):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Invalid Id')
        elif response < 0:
            return IResponse(
                message=f'User with id: {id} not found',
                response=False,
                status=StatusMessage.NOT_SUCCESSFUL
            )
        return IResponse(
            message=f'User with id: {id}  deleted',
            response=True,
            status=StatusMessage.DELETED
        )
