from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<product_id>/', views.product_detail, name='product_detail'),
    path('workshop/', views.workshop, name='workshop'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<product_id>/', views.delete_product, name='delete_product'),
    path('edit_service/<product_id>/', views.edit_service, name='edit_service'),
    path('delete_service/<product_id>/', views.delete_service, name='delete_service'),
]