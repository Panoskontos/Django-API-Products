
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('products', products, name='products'),
    path('products/<str:pk>', product, name='product'),
    path('create_product', create_product, name='create_product'),
    path('update_product/<str:pk>', update_product, name='update_product'),
    path('delete_product/<str:pk>', delete_product, name='delete_product'),

]