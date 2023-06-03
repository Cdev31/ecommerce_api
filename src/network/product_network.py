from fastapi import (responses,HTTPException,Request)
from bson import errors
from starlette import status

#internal networks
from Interfaces.response_types import IResponse,StatusMessage
from service.product_service import Service

product_service = Service()

class NetworkProduct:

    def find(self):
        return product_service.find_products()

    def find_one(self,id:str):
            product = product_service.find_one_product(id)
            if product == None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'Product with id: {id} not found')
            
            elif isinstance(product,errors.InvalidId):
                return responses.JSONResponse(status_code=400,content='Invalid Id')
        
            return IResponse(
                    message='Product Found',
                    response=product,
                    status= StatusMessage.SUCCESS
                    )
    
    def create(self,body:dict,req:Request): 
        for i,file in enumerate(body['images_products']):
            body['images_products'][i] = f'http://192.168.0.23:3000/public/imgProducts/{file}'    
        new_product = product_service.create_product(body)
        return new_product


    def update(self,id:str,changes:dict):
            product = product_service.update_info_product(id,changes)
            if product == None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'Product with id: {id} not found')
            
            elif isinstance(product,errors.InvalidId):
                return responses.JSONResponse(status_code=400,content='Invalid Id')
        
            return IResponse(
                    message='Product Updated',
                    response=product,
                    status= StatusMessage.UPDATED
                    )
    
    def delete(self,id:str):
        product = product_service.delete_product(id)

        if product < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Product with id: {id} not found')
            
        elif isinstance(product,errors.InvalidId):
            return responses.JSONResponse(status_code=400,content='Invalid Id')
        
        return IResponse(
                message='Product Deleted',
                response=True,
                status= StatusMessage.DELETED
                )
                    