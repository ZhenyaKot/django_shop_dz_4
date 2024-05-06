from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Order, Product
from django.views.generic import TemplateView
from django.utils import timezone


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


class ProductOrder(TemplateView):
    template_name = 'shopapp/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(id=3)
        orders_last_week = Order.objects.filter(client=client,
                                                date_of_order__gte=timezone.now() - timezone.timedelta(days=7))
        orders_last_month = Order.objects.filter(client=client,
                                                 date_of_order__gte=timezone.now() - timezone.timedelta(days=30))
        orders_last_year = Order.objects.filter(client=client,
                                                date_of_order__gte=timezone.now() - timezone.timedelta(days=365))

        products_last_week = Product.objects.filter(order__in=orders_last_week).distinct()
        products_last_month = Product.objects.filter(order__in=orders_last_month).distinct()
        products_last_year = Product.objects.filter(order__in=orders_last_year).distinct()

        context['last_week'] = products_last_week
        context['last_month'] = products_last_month
        context['last_year'] = products_last_year

        return context
