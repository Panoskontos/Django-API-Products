
from django.contrib import admin
from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(r'products', ProductViewSet, basename='product')
router.register(r'movies', ModelViewSet, basename='movie')
urlpatterns = router.urls

# GET products Read
# POST products Create
# GET products/id Read
# PUT products/id Update
# DELETE products/id Delete





# urlpatterns = [
    # path('products', products, name='products'),
    # path('products/<str:pk>', product, name='product'),
    # path('create_product', create_product, name='create_product'),
    # path('update_product/<str:pk>', update_product, name='update_product'),
    # path('delete_product/<str:pk>', delete_product, name='delete_product'),

# ]