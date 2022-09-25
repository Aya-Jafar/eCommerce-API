'''
A file for some helper functions
'''

from django.contrib.auth import get_user_model
from .models import Favorite

User = get_user_model()


def handle_products(all_products, request):
    result = []
    for product in all_products:
        result.append(product.__dict__)
        convert_dtypes(product)
        product.__dict__['is_favourite'] = is_favourite(
            product, request.auth['pk'])
    return result


def handle_product(product, request):
    convert_dtypes(product)
    product.__dict__['is_favourite'] = is_favourite(
        product, request.auth['pk'])


def is_favourite(product, user_id):
    try:
        if Favorite.objects.get(product__id=product.id, user__id=user_id) \
                in User.objects.get(id=user_id).favorites.all():
            is_favourite = True

    except Favorite.DoesNotExist:
        is_favourite = False

    return is_favourite


def convert_dtypes(product):
    product.__dict__['colors'] = list(product.colors.values_list('name', flat=True))
    product.__dict__['rams_and_storage'] = list(product.rams_and_storage.values_list('name', flat=True))
    product.__dict__['product_images'] = list(product.product_images.values_list('image', flat=True))



def handle_fav_products(related_objects):
    result = []
    for i in related_objects:
        i.product.__dict__['id'] = i.id
        result.append(i.product.__dict__)
        convert_dtypes(i.product)
    return result
    


def handle_items(items):
    items_out = []
    for i in items:
        i.product.__dict__['id'] = i.id # make the id of the product id of the item
        items_out.append(i.product.__dict__)
        i.product.__dict__['quantity'] = i.quantity
        convert_dtypes(i.product)

    return items_out