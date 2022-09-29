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
        convert_dtypes(product)
        result.append(product.__dict__)
    return result



def convert_dtypes(product):
    product.__dict__['colors'] = list(product.colors.values_list('name', flat=True))
    product.__dict__['rams_and_storage'] = list(product.rams_and_storage.values_list('name', flat=True))
    product.__dict__['product_images'] = list(product.product_images.values_list('image', flat=True))



def handle_related_objects(related_objects):
    result = []

    for i in related_objects:
        convert_dtypes(i.product)
        if type(i) is Item:
            result.append({
                'id': i.id,
                'total': i.get_item_total,
                'quantity': i.quantity,
                'product': i.product.__dict__,
            })
        else:
            result.append({
                'id': i.id,
                'product': i.product.__dict__,
            })
    return result
