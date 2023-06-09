from pydantic import BaseModel
from typing import Generic,TypeVar,Dict,List
from enum import Enum

#messages status
class StatusMessage(Enum):
    SUCCESS = 'SUCCESS'
    CREATED = 'CREATED'
    DELETED = 'DELETED'
    UPDATED = 'UPDATED'
    NOT_SUCCESSFUL = 'NOT SUCCESFUL'

T= TypeVar('T',bound=Dict | List[dict] | bool)

class IResponse(BaseModel,Generic[T]):
    message: str
    status: StatusMessage
    response: T
   

