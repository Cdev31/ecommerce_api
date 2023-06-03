from fastapi import FastAPI,responses
from fastapi.staticfiles import StaticFiles
import uvicorn

#import of router api function
from router.index_router import api_router

        
app: FastAPI = FastAPI(redoc_url=None)

app.title = 'Ecommerce Api'
app.version = '1.0.0'
app.description = """<strong>Api whose purpose is to serve products for an ecommerce, 
                     user authentication, among other functionalities<strong/>"""

app.mount('/public', StaticFiles(directory= 'public') , name='public')


@app.get('/',tags=['Home'])
def home():
    return responses.FileResponse('public/index.html')

api_router(app)

if __name__ =='__main__':
    uvicorn.run("server:app",host='localhost',port=3000,reload=True,log_level='info')