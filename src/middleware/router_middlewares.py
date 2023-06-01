from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

#internal imports 
from schemas.product_schema import change_dinamic_category,CreateProductSchema
from utils.types import Categories

async def validate_category(req:Request,call_next):
    response = await call_next(req)
    if req.method == 'POST' and req.url.path== '/api/v1/Product':
        try:
            product = await req.json()
            for c in Categories.__str__():
                if product['category'] == c:
                   change_dinamic_category[product['category']](**product)
                   break
            else: 
                raise ValueError('Invalid Category')
        except ValidationError as e:
            response = {'details': e.errors()}
            return JSONResponse(status_code=400,content=response)
    return response

def setup_middleware(app:FastAPI):
    app.middleware('http')(lambda req,call_next: validate_category(req,call_next))       