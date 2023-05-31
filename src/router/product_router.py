from fastapi import APIRouter,HTTPException,Request

from service.product_service import Service 

user_service: Service = Service()

router = APIRouter(tags=['Products'])

@router.get('/')
def find_products():
    response = user_service.find_products()
    return response


@router.get('/{id}')
def find_product():
    return {'hi','hello'}

@router.post('/')
def create_product():
    return {'hi','hello'}


@router.patch('/')
async def update_product():
    return {'hi':'hello'}


@router.delete('/')
def delete_product():
    return {'hi','hello'}
