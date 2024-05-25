from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description='Обнулить кол-во')
def prob_action(modeladmin, request, queryset):
    queryset.update(quantity=0)


class AdminClient(admin.ModelAdmin):
    list_display = ['name', 'email',
                    'phone_number',
                    ]
    list_filter = ['name', ]
    search_fields = ['name', 'email', 'phone_number']
    fields = ['name', 'email', 'phone_number', 'address', 'date_of_register']
    readonly_fields = ['name', ]


class AdminProduct(admin.ModelAdmin):
    list_display = ['name_product',
                    'price',
                    'quantity',
                    'date_added',
                    ]
    list_filter = ['price', 'date_added']
    search_fields = ['name_product', 'price', 'date_added']
    fields = ['name_product', 'price', 'quantity', 'date_added', 'description']
    readonly_fields = ['description', ]
    actions = [prob_action,]


class AdminOrder(admin.ModelAdmin):
    list_display = ['client',
                    'product',
                    'date_of_order',
                    ]
    list_filter = ['client', 'product', 'date_of_order']
    search_fields = ['client', 'product', 'date_of_order']
    fields = ['client', 'product', 'date_of_order', 'total_sum']


admin.site.register(Client, AdminClient)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
