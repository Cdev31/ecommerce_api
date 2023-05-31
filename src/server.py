from fastapi import FastAPI,Request
import uvicorn

#import of router api function
from router.index_router import api_router


app: FastAPI = FastAPI(redoc_url=None)

app.title = 'Ecommerce Api'
app.version = '1.0.0'
app.description = """<strong>Api whose purpose is to serve products for an ecommerce, 
                     user authentication, among other functionalities<strong/>"""


@app.get('/',tags=['Home'])
def home():
    return {'hello': 'world'}

api_router(app)

if __name__ =='__main__':
    uvicorn.run("server:app",host='localhost',port=3000,reload=True)