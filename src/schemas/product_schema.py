from pydantic import  BaseModel,Field,validator
from typing import List,Optional,Tuple
from fastapi import Form,File,UploadFile

class CreateProductSchema(BaseModel):
    title: str = Form()
    stock: int = Form(ge=5)
    price: float = Form(ge=1)
    category: str = Form()
    images_products: List[UploadFile] = File()
    brand: str= Form()

    @validator('price','stock',pre=True)
    def validate_price(cls,value): 
        if value == True or isinstance(value,str):
            raise ValueError('price must be a int')
        return value
    
class UpdateProductSchema(BaseModel):
    title: Optional[str] = Field()
    stock: Optional[int] = Field()
    price: Optional[float] = Field()
    category: str = Field()
    images_products: Optional[List[str]] = Field()
    brand: Optional[str] = Field()


#informacion altern requerida dependiendo de la categoria

class ElectronicProductSchema(CreateProductSchema):
    ram: str = Form()
    processor: str = Form()
    screen_size: str = Form()
    operative_system: str = Form()
    model: str = Form()

class CleaningProductSchema(CreateProductSchema):
    expiration: str = Form()
    range_age: Tuple[int,int] = Form()
    indications: str = Form()
    quantity: str = Form()
    package_size: str = Form()

class PersonalCareProductSchema(CleaningProductSchema):
    flavor: Optional[str] = Form()
    smell: Optional[str] = Form()
    item_shape: str = Form()


class ClotheShoesProductSchema(CreateProductSchema):
    size: str = Field()
    gender: str = Field()


change_dinamic_category = {
    'Cleaning': CleaningProductSchema,
    'Electronic': ElectronicProductSchema,
    'Peronal_Care': PersonalCareProductSchema,
    'Clothes': ClotheShoesProductSchema,
    'Shoes': ClotheShoesProductSchema,
    'Others': CreateProductSchema
}