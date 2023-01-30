from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_basket, name='basket'),
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<product_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('on_stock/<int:product_id>/', views.adjust_qty_on_stock, name='adjust_qty_on_stock'),
]