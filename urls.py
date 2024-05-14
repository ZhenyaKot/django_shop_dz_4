from django.urls import path, include
from .views import index, create_client, create_order, create_product, product_photo
from .views import ProductOrder

urlpatterns = [
    path('', index, name='index'),
    path('create_client', create_client, name='create_client'),
    path('create_order', create_order, name='create_order'),
    path('create_product', create_product, name='create_product'),
    path('product/order/', ProductOrder.as_view(), name='product_order'),
    path('/product_photo/', product_photo, name='product_photo'),

]
