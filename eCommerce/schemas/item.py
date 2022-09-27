from typing import Dict, List
from pydantic.networks import EmailStr
from .product import Product
from ninja import Schema



class OrderItemOut(Schema):
    id : int 
    status : str


class ItemsOut(Product):
    # item_id : int
    # product: Product
    quantity : int
    total : float


class ItemIn(Schema):
    product_id : int
    quantity : int 

