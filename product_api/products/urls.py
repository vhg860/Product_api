from django.urls import path
from .views import product_list_create, index

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list_create, name='product-list-create'),
]
