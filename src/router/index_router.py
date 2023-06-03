from fastapi import APIRouter

#internal imports router
from router.user_router import router as router_user
from router.product_router import router as router_product
from router.auth_router import router as router_auth
from router.category_router import router as router_category

#internal imports middlewares
from middleware.router_middlewares import setup_middleware

def api_router(app):
    setup_middleware(app)
    
    router = APIRouter(prefix='/api/v1')
    router.include_router(prefix='/User',router=router_user)
    router.include_router(prefix='/Product',router=router_product)
    router.include_router(prefix='/Auth',router=router_auth)
    router.include_router(prefix='/category',router=router_category)
    app.include_router(router)


    
    
    