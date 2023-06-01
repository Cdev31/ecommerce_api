from pydantic import BaseModel
from typing import Generic,TypeVar,Dict
from enum import Enum

#messages status
class StatusMessage(Enum):
    SUCCESS = 'SUCCESS'
    CREATED = 'CREATED'
    DELETED = 'DELETED'
    UPDATED = 'UPDATED'
    NOT_SUCCESSFUL = 'NOT SUCCESFUL'

T= TypeVar('T',bound=Dict[str,str | list | dict])

class IResponse(BaseModel,Generic[T]):
    response: T
    message: str
    status: StatusMessage

