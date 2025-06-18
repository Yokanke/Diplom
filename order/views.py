from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from basket.basket import Basket


def o_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            if not form.cleaned_data['phone_number'].startswith("+7"):
                return render(request, 'order/create.html', {'basket': basket, 'form': form, 'title': 'Оформление заказа', 'error': 'Номер должен начинаться с +7' })

            order = form.save()

            for item in basket:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            basket.clear()
            return render(request, 'order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'order/create.html', {'basket': basket, 'form': form, 'title': 'Оформление заказа'})