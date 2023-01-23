from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('workshop/', views.workshop, name='workshop'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    # path('subtract_products/<int:product_id>/<int:number>/', views.subtract_products, name='subtract_products'),

]