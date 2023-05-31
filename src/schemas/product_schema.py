from pydantic import  BaseModel,Field
from typing import List,Optional,Tuple

class CreateProductSchema(BaseModel):
    title: str = Field()
    stock: int = Field()
    price: float = Field()
    images_products: List[str] = Field()
    brand: str= Field()

class UpdateProductSchema(BaseModel):
    title: Optional[str] = Field()
    stock: Optional[int] = Field()
    price: Optional[float] = Field()
    category: str = Field()
    images_products: Optional[List[str]] = Field()
    brand: Optional[str] = Field()


#informacion altern requerida dependiendo de la categoria

class ElectronicProductSchema(CreateProductSchema):
    ram: str = Field()
    processor: str = Field()
    screen_size: str = Field()
    operative_system: str = Field()
    model: str = Field()

class CleaningProductSchema(CreateProductSchema):
    expiration: str = Field()
    range_age: Tuple[int,int] = Field()
    indications: str = Field()
    quantity: str = Field()
    package_size: str = Field()

class PersonalCareProductSchema(CleaningProductSchema):
    flavor: Optional[str] = Field()
    smell: Optional[str] = Field()
    item_shape: str = Field()


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