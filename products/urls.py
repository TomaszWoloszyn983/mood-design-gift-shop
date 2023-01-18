from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<product_id>/', views.product_detail, name='product_detail'),
    path('workshop/', views.workshop, name='workshop'),
]