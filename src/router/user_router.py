from fastapi import APIRouter,Path,Body
from starlette import status

#internal imports
from schemas.user_schema import CreateUserSchema,ResponseModel
from network.user_network import UserNetwork

router = APIRouter(tags=['Users'])
user_network = UserNetwork()

@router.get('/',status_code=status.HTTP_200_OK)
async def find_users():
    response =  user_network.finds()
    return response


@router.get('/{id}',status_code=status.HTTP_202_ACCEPTED)
def find_user(id:str = Path()):
    response = user_network.find_one(id)
    return response


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=ResponseModel)
def create_user(body: CreateUserSchema ):
    response = user_network.create(dict(body))
    print(type(response.response['role']))
    return response


@router.patch('/{id}')
def update_user(id:str = Path(),changes = Body()):
    response = user_network.update(id,changes)
    return response


@router.delete('/{id}')
def delete_user(id: str  = Path()):
    response = user_network.delete(id)
    return response
