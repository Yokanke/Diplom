from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .basket import Basket
from .forms import *


@require_POST
def b_add(request, shop_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=shop_id)
    form = AddBasketForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('/')


def b_fast_buy(request, shop_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=shop_id)
    clear_cart = Product.objects.all()
    for item in clear_cart:
        basket.remove(item)
    form = AddBasketForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('o_create')

def b_remove(request, shop_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=shop_id)
    basket.remove(product)
    return redirect('b_detail')


def b_detail(request):
    basket = Basket(request)
    return render(request, 'basket/basket.html', {'basket': basket, 'title': 'Корзина'})
