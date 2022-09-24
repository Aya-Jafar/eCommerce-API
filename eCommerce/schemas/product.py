from ninja import Schema
from typing import List


class AbstractProductProperty(Schema):
    name:str

class ProductColorOut(AbstractProductProperty):
    pass

class ProductRamStorage(AbstractProductProperty):
    pass
    

class Product(Schema):
    id : int
    name : str
    price : float
    catogary : str
    brand : str 
    rate : float
    colors : List[str]
    rams_and_storage : List[str] 
    cpu : str 
    system : str
    is_best_selling : bool 
    is_trending_now : bool
    product_images : List[str] 



class ProductOut(Product):
    is_favourite : bool


class FavProductOut(Schema):
    product : Product 

class FourOFour(Schema):
    message : str


class ImgOut(Schema):
    id : int 
    image : str


Product.update_forward_refs()
ProductOut.update_forward_refs()


