from django.urls import path

from .views import *

urlpatterns = [
    path('create/', o_create, name='o_create'),
]