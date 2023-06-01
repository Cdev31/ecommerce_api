from fastapi import APIRouter,Path,Request
from starlette import status
from network.product_network import NetworkProduct

user_network = NetworkProduct()
router = APIRouter(tags=['Products'])


@router.get('/',status_code=status.HTTP_200_OK)
def find_products():
    response = user_network.find()
    return response


@router.get('/{id}')
def find_product(id: str = Path()):
    response = user_network.find_one(id)
    return response

@router.post('/')
async def create_product(req:Request):
    new_product = await req.json()
    response = user_network.create(new_product)
    return response
  


@router.patch('/{id}')
async def update_product(req:Request,id:str = Path()):
    changes = await req.json()
    response = user_network.update(id,changes)
    return response


@router.delete('/{id}')
def delete_product(id: str = Path()):
    response = user_network.delete(id)
    return response
