from abc import ABC,abstractmethod
from Interfaces.response_types import IResponse

class InterfaceProduct(ABC):
    @abstractmethod
    def find_products(self) -> IResponse:
        pass
    
    @abstractmethod
    def find_one_product(self,id:str) -> IResponse:
        pass
    
    @abstractmethod
    def create_product(self,body:dict) -> IResponse:
        pass
    
    @abstractmethod
    def update_info_product(self,id:str,chages:dict) -> IResponse:
        pass
    
    @abstractmethod
    def delete_product(self,id:str) -> IResponse:
        pass
