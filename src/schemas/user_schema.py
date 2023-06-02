from pydantic import BaseModel,Field,EmailStr,validator
from typing import Optional
import datetime

#internal imports
from utils.types import Roles
from Interfaces.response_types import StatusMessage

class CreateUserSchema(BaseModel):
    first_name: str = Field(min_length=3,max_length=10)
    last_name: str = Field(min_length=3,max_length=10)
    username: str = Field(min_length=5)
    email: EmailStr = Field()
    date_of_birth: datetime.date = Field()
    password: str = Field(regex='^(?=.*[A-Za-z0-9])(?=.*[!@])[A-Za-z0-9@!]{8,15}$')
    confirm_password: str = Field(regex='^(?=.*[A-Za-z0-9])(?=.*[!@])[A-Za-z0-9@!]{8,15}$')
    role: Roles = Field(default=Roles.Normal.value)

    @validator('confirm_password')
    def validate_password(cls,value,values):
        if value != values['password']:
            raise ValueError('Confirm_password is not equal password')
        return value 

class ResponseModelUser(BaseModel):
    id: str 
    username: str 
    email: str
    date_of_birth: datetime.datetime
    role: Roles

class ResponseModel(BaseModel):
    message: str
    status: StatusMessage
    response: list[ResponseModelUser] | ResponseModelUser
   

class UpdateInfoUserSchema(BaseModel):
    first_name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    username: Optional[str] = Field()
    password: Optional[str] = Field()
    confirm_password: Optional[str] = Field()
    role: Optional[Roles] = Field()
    image_url: Optional[str] = Field()
    
class AddPhotoUserSchema(BaseModel):
    image_url: str = Field()    

    