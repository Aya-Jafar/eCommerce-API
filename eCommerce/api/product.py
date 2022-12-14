
from datetime import datetime
from django.contrib.auth import get_user_model
from restauth.authorization import AuthBearer
from rest_framework import status
from eCommerce.schemas.product import ProductOut, FourOFour, ImgOut
from ..models import Item, Order, Product, ProductImage
from ..choices import ProductBrand, ProductCatogary
from eCommerce.schemas.product import Product as ProductSchema
from typing import List
from ninja import Router
from ..services import convert_dtypes,  handle_products


product_router = Router(tags=['Product'])


User = get_user_model()



@product_router.get('get-all/', response=List[ProductOut], auth=AuthBearer())
def get_all_products(request):
    all_products = Product.objects.order_by('-id')
    result = handle_products(all_products, request)
    return result


@product_router.get('get-product-by-id/', response={
    200: ProductOut,
    404: FourOFour
}, auth=AuthBearer())
def get_product_by_id(request, id: int):
    try:
        product = Product.objects.get(id=id)
        convert_dtypes(product)
        return status.HTTP_200_OK, product.__dict__

    except Product.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'message': f'Product with id {id} does not exist'}



@product_router.get('get-product-by-name/', response={
    200: ProductOut,
    404: FourOFour
}, auth=AuthBearer())
def get_product_by_name(request, name: str):
    try:
        product = Product.objects.get(name=name)
        convert_dtypes(product)
        return status.HTTP_200_OK, product.__dict__
    except Product.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'message': f'{name} product does not exist'}


@product_router.get('filter-phones/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_phones(request):
    filtered = Product.objects.order_by('-id').filter(catogary='Phones')
    if filtered:
        filtered = handle_products(filtered, request)
        return status.HTTP_200_OK, filtered

    return status.HTTP_404_NOT_FOUND, {'message': 'No products in Phones catogary'}


@product_router.get('filter-laptops/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_laptops(request):
    filtered = Product.objects.order_by('-id').filter(catogary='Laptops')
    if filtered:
        filtered = handle_products(filtered, request)
        return status.HTTP_200_OK, filtered

    return status.HTTP_404_NOT_FOUND, {'message': 'No products in Laptops catogary'}


@product_router.get('filter-tablets/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_tablets(request):
    filtered = Product.objects.order_by('-id').filter(catogary='Tablets')
    if filtered:
        filtered = handle_products(filtered, request)
        return status.HTTP_200_OK, filtered

    return status.HTTP_404_NOT_FOUND, {'message': 'No products in Tablets catogary'}


@product_router.get('filter-desctop-pc/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_pc(request):
    filtered = Product.objects.order_by('-id').filter(catogary='Desktop pc')
    if filtered:
        filtered = handle_products(filtered, request)
        return status.HTTP_200_OK, filtered
   
    return status.HTTP_404_NOT_FOUND, {'message': 'No products in Desktop pc catogary'}



@product_router.get('get-trending-products/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_trending_products(request):
    trending_products = Product.objects.order_by(
        '-id').filter(is_trending_now=True)
    if trending_products:
        trending_products = handle_products(trending_products, request)
        return status.HTTP_200_OK, trending_products
    return status.HTTP_404_NOT_FOUND, {'message': 'No trending products found'}


@product_router.get('get-best-selling-products/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_best_selling_products(request):
    best_selling = Product.objects.order_by('-id').filter(is_best_selling=True)
    if best_selling:
        best_selling = handle_products(best_selling, request)
        return status.HTTP_200_OK, best_selling
    return status.HTTP_404_NOT_FOUND, {'message': 'No best selling products found'}



@product_router.get('filter-by-brand/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_by_brand(request, to_filter_by: str):
    choices = [i[0] for i in ProductBrand.choices]
    if to_filter_by in choices:
        filtered = Product.objects.filter(brand__iexact=to_filter_by)
        filtered = handle_products(filtered, request)
        return status.HTTP_200_OK, filtered
  
    return status.HTTP_404_NOT_FOUND, {'message': f'No brand named {to_filter_by}'}


@product_router.get('filter-by-price/', response={
    200: List[ProductOut],
    404: FourOFour
}, auth=AuthBearer())
def filter_by_price(request, min: int, max: int):
    filtered = Product.objects.filter(price__in=range(min, max+1))
    if filtered:
        filtered = handle_products(filtered, request)
        return status.HTTP_200_OK, filtered
    
    return status.HTTP_404_NOT_FOUND, {'message': f'No products found with price range {min} - {max}'}



@product_router.get('product-images/', response=List[ImgOut], auth=AuthBearer())
def get_product_images(request):
    return ProductImage.objects.select_related('product').all()
