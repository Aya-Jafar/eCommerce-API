'''
A file for some helper functions
'''

from django.contrib.auth import get_user_model
from .models import Favorite, Item

User = get_user_model()


def is_favourite(product, user_id):
    try:
        if Favorite.objects.get(product__id=product.id, user__id=user_id) \
                in User.objects.get(id=user_id).favorites.all():
            is_favourite = True

    except Favorite.DoesNotExist:
        is_favourite = False

    return is_favourite



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


def convert_dtypes(product):
    product.__dict__['colors'] = list(product.colors.values_list('name', flat=True))
    product.__dict__['rams_and_storage'] = list(product.rams_and_storage.values_list('name', flat=True))
    product.__dict__['product_images'] = list(product.product_images.values_list('image', flat=True))



def handle_related_objects(related_objects):
    result = []
    for i in related_objects:
        convert_dtypes(i.product)
        i.product.__dict__['id'] = i.id
        result.append(i.product.__dict__)

        if type(related_objects[0]) is Item:
            i.product.__dict__['quantity'] = i.quantity
            i.product.__dict__['total'] = i.get_item_total


        # i.product.__dict__['product'] = i.product.__dict__
        # result.append(i.product.__dict__['product'])
        # convert_dtypes(i.product)
        
        # if type(related_objects[0]) is Item:
        #     i.product.__dict__['item_id'] = i.id 
        #     i.product.__dict__['quantity'] = i.quantity
        #     i.product.__dict__['total'] = i.get_item_total

        # elif type(related_objects[0]) is Favorite:   
        #     i.product.__dict__['fav_id'] = i.id

    return result
