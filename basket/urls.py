from django.urls import path

from .views import *

urlpatterns = [
    path('', b_detail, name='b_detail'),
    path('add/<int:shop_id>', b_add, name='b_add'),
    path('buy/<int:shop_id>', b_fast_buy, name='b_fast_buy'),
    path('remove/<int:shop_id>', b_remove, name='b_remove'),
]
