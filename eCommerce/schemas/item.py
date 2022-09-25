from typing import Dict, List
from pydantic.networks import EmailStr
from .product import Product
from ninja import Schema



class OrderItemOut(Schema):
    id : int 
    status : str


class ItemsOut(Product):
    # product:Product
    id : int
    quantity : int


class ItemIn(Schema):
    product_id : int
    quantity : int 


