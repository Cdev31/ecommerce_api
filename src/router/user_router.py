from fastapi import APIRouter,HTTPException

router = APIRouter(tags=['Users'])

@router.get('/')
def find_users():
    return {'hi','hello'}


@router.get('/{id}')
def find_user():
    return {'hi','hello'}


@router.post('/')
def create_user():
    return {'hi','hello'}


@router.patch('/')
def update_user():
    return {'hi','hello'}


@router.delete('/')
def delete_user():
    return {'hi','hello'}
