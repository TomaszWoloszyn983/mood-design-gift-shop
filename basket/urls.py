from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_basket, name='basket'),
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
]