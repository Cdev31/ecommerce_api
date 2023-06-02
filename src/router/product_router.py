from fastapi import APIRouter,Path,Request,Body
from starlette import status
from network.product_network import NetworkProduct

#internal imports
from schemas.product_schema import UpdateProductSchema

user_network = NetworkProduct()
router = APIRouter(tags=['Products'])


@router.get('/',status_code=status.HTTP_200_OK)
def find_products():
    response = user_network.find()
    return response


@router.get('/{id}',status_code=status.HTTP_200_OK)
def find_product(id: str = Path()):
    response = user_network.find_one(id)
    return response

@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_product(req:Request):
    new_product = await req.json()
    response = user_network.create(new_product)
    return response
  


@router.patch('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update_product(id:str = Path(),changes:UpdateProductSchema = Body()):
    response = user_network.update(id,dict(changes))
    return response


@router.delete('/{id}',status_code=status.HTTP_202_ACCEPTED)
def delete_product(id: str = Path()):
    response = user_network.delete(id)
    return response
