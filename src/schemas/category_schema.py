from pydantic import BaseModel,Field
from typing import Optional

class CreateCategory(BaseModel):
    name_category: str = Field()
    description: str = Field()

class UpdateCategory(BaseModel):
    name_category: Optional[str] = Field()
    description: Optional[str] = Field()

    