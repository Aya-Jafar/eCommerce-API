from ninja import Schema
from restauth.schemas import AccountOut
from typing import List
# from .product import ProductOut

class ItemOutForCard(Schema):
    product_id : int
    quantity : int


class TotalCardOut(Schema):
    total : float  


class CartOut(Schema):
    id : int
    owner : AccountOut
    items: List[ItemOutForCard]
    # total : float
    # quantity : int


class CardQntOut(Schema):
    total_qnt: int 


class MessageOut(Schema):
    detail:str

class OrderIn(Schema):
    items: List[int] 
