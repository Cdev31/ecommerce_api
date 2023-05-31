from pydantic import BaseModel,Field
from typing import Optional
import datetime

class CreateUserSchema(BaseModel):
    first_name: str = Field()
    last_name: str = Field()
    username: str = Field()
    email: str = Field()
    password: str = Field()
    confirm_password: str = Field()
    role: str = Field()

class UpdateInfoUserSchema(BaseModel):
    first_name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    username: Optional[str] = Field()
    email: Optional[str] = Field()
    password: Optional[str] = Field()
    confirm_password: Optional[str] = Field()
    role: Optional[str] = Field()
    date_of_birth: datetime.date = Field()
    image_url: Optional[str] = Field()
    
class AddPhotoUserSchema(BaseModel):
     image_url: str = Field()    

    