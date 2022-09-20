from django.contrib.auth import get_user_model
from .models import Favorite

User = get_user_model()


def handle_products(all_products,request):
    result = []
    for product in all_products:
        result.append(product.__dict__)
        convert_dtypes(product)
        product.__dict__['is_favourite'] = is_favourite(product, request.auth['pk'])
    return result


def handle_product(product,request):
    product.__dict__['is_favourite'] = is_favourite(product, request.auth['pk'])



def is_favourite(product,user_id):
    try:
        if Favorite.objects.get(product__id=product.id, user__id=user_id) \
                in User.objects.get(id=user_id).favorites.all():
            is_favourite = True

    except Favorite.DoesNotExist:
        is_favourite = False

    return  is_favourite


def convert_dtypes(product):
    product.__dict__['colors']= list(product.colors.all())
    product.__dict__['rams_and_storage'] = list(product.rams_and_storage.all())
    product.__dict__['product_images'] = list(product.product_images.all())


    

