from django.db import models
from store.models import *


class Order(models.Model):
    first_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    house = models.CharField(max_length=10)
    flat = models.CharField(max_length=5)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __int__(self):
        return self.pk

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT, verbose_name='Отношение к заказу')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT, verbose_name='Что заказано')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'

    def __int__(self):
        return self.pk

    def get_cost(self):
        return self.price * self.quantity

    