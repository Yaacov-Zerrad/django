from django.urls import path
from products.views import product_list, index2, blog, contact, product_create, product_manager, product_update, product_delete


urlpatterns = [
    path('', product_list, name='index'),
    path('manager/', product_manager, name='manager'),
    path('create/', product_create, name='create'),
    path('update/<int:pk>', product_update, name='update'),
    path('delete/<int:myid>', product_delete, name='delete'),
]