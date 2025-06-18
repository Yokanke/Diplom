from django.contrib import admin
from .models import *

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']
    list_filter = ['id', 'order']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'city', 'street', 'house', 'flat', 'email', 'phone_number', 'time_created', 'updated']
    list_filter = ['time_created', 'updated']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)