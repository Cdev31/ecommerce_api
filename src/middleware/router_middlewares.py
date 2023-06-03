from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

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
                'images_products': name_files_products(product.getlist('image'),req)
            }

            for c in Categories.__str__():
                if product['category'] == c:
                   change_dinamic_category[str(product['category'])](**{**product._dict,**new_product})
                   validation_pased = True
                   break
            else: 
                return JSONResponse(status_code=400,content='Invalid Category')
            
            if validation_pased == True:
                create_files(product.getlist('image'),new_product['images_products'])
            
            del product._dict['image']     
            req.app.state.product = str({**product._dict,**new_product})

        except ValidationError as e:
            response = {'details': e.errors()}
            return JSONResponse(status_code=400,content=response)
        
        except KeyError as e:
            response = {'details':f'{e.args} is required'}
            return JSONResponse(status_code=400,content=response)
    return response

def setup_middleware(app:FastAPI):
    app.middleware('http')(validate_category)       