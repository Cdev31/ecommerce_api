from pydantic import BaseModel
from typing import Generic,TypeVar,Dict

T= TypeVar('T',bound=Dict[str,str | list | dict])

class IResponse(BaseModel,Generic[T]):
    response: T
    message: str

