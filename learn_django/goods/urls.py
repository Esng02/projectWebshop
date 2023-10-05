from django.urls import path
from . import views

urlpatterns = [
    path('', views.goods_index, name='goods_index'),
    path('add', views.add_product, name='add_product')
]