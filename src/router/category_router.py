from fastapi import APIRouter,HTTPException

router = APIRouter(tags=['Category'])

@router.get('/')
def find_categories():
    return {'hi','hello'}


@router.post('/')
def create_category():
    return {'hi','hello'}


@router.patch('/')
def update_category():
    return {'hi','hello'}

