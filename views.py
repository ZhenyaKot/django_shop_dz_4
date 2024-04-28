from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Order, Product


def index(request):
    return HttpResponse('Hello world')


def create_client(request):
    for i in range(1, 20):
        client = Client(name=f'{i * 5}', email=f'aaaa@{i}',
                        phone_number=f'8900{i * 11}', address=f'{i}', date_of_register=f'2024-04-29')
        client.save()
    return HttpResponse('create_client')


def create_product(request):
    for i in range(1, 20):
        product = Product(name_product=f'{i * 5}', price=f'{i * 500}',
                          description=f'{i}', date_added=f'2024-04-29', quantity=i * 22)
        product.save()
    return HttpResponse('create_product')


def create_order(request):
    for i in range(1, 20):
        order = Order(total_sum=f'{i * 500}', date_of_order=f'2024-04-29',
                      client_id=i, product_id=i)
        order.save()
    return HttpResponse('create_order')


