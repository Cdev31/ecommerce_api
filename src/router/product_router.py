from fastapi import APIRouter,Path,Body,Request
from starlette import status
from network.product_network import NetworkProduct
import ast
#internal imports
from schemas.product_schema import UpdateProductSchema

product_network = NetworkProduct()
router = APIRouter(tags=['Products'])


@router.get('/',status_code=status.HTTP_200_OK)
def find_products():
    response = product_network.find()
    return response


@router.get('/{id}',status_code=status.HTTP_200_OK)
def find_product(id: str = Path()):
    response = product_network.find_one(id)
    return response

@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_product(req:Request):
    product = ast.literal_eval(req.app.state.product)
    response = product_network.create(product,req)
    return response
  


@router.patch('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update_product(id:str = Path(),changes:UpdateProductSchema = Body()):
    response = product_network.update(id,dict(changes))
    return response


@router.delete('/{id}',status_code=status.HTTP_202_ACCEPTED)
def delete_product(id: str = Path()):
    response = product_network.delete(id)
    return response
