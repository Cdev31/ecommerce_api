from abc import ABC,abstractmethod
from typing import List,Any
from bson.errors import InvalidId

class InterfaceUser(ABC):

    @abstractmethod
    def find_users(self) -> List[dict]:
        pass

    @abstractmethod
    def find_user(self,id:str) -> dict:
        pass

    @abstractmethod
    def create_user(self,body:dict) -> dict:
        pass

    @abstractmethod
    def update_user(self,id:str,changes:dict) -> dict:
        pass

    @abstractmethod
    def delete_user(self,id:str) -> int | InvalidId :
        pass