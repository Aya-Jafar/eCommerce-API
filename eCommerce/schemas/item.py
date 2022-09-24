from typing import Dict, List
from pydantic.networks import EmailStr
from .product import Product
from ninja import Schema



class OrderItemOut(Schema):
    id : int 
    status : str

class ItemsOut(Schema):
    id : int
    # product: Product
    product_id : int
    # order : OrderItemOut
    quantity : int


class ItemIn(Schema):
    product_id : int
    quantity : int 


