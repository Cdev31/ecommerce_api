from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import datetime

#internal imports 
from schemas.product_schema import change_dinamic_category
from utils.handler_image import name_files_products,create_files
from utils.types import Categories

async def validate_category(req:Request,call_next):
    response = await call_next(req)
    if req.method == 'POST' and req.url.path== '/api/v1/Product':
        try:
            product = await req.form()
            validation_pased = False

            new_product = {
                'stock': int(str(product['stock'])),
                'price': float(str(product['price'])),
                'images_products': name_files_products(product.getlist('image'))
            }

            for c in Categories.__str__():
                if product['category'] == c:
                   change_dinamic_category[str(product['category'])](**{**product._dict,**new_product})
                   validation_pased = True
                   break
            else: 
                raise ValueError('Invalid Category')
            
            if validation_pased == True:
                create_files(product.getlist('image'),new_product['images_products'])

        except ValidationError as e:
            response = {'details': e.errors()}
            return JSONResponse(status_code=400,content=response)
    return response

def setup_middleware(app:FastAPI):
    app.middleware('http')(lambda req,call_next: validate_category(req,call_next))       