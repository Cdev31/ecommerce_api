from enum import Enum

#categories Types
class Categories(Enum):
    Electronic = 'Electronic'
    Cleaning = 'Cleaning'
    Clothes = 'Clothes'
    Shoes = 'Shoes'
    Personal_Care = 'Personal Care'
    Others = 'Others'

    @classmethod
    def __str__(cls):
        return list(Categories.__members__)   
    
    