from fastapi import APIRouter,HTTPException

router = APIRouter(tags=['Auth'])

@router.post('/Log_in')
def log_in():
    return {'hi','hello'}


@router.post('/Register')
def register():
    return {'hi','hello'}


@router.post('/Change_password')
def change_password():
    return {'hi','hello'}

