from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('send_post/', views.send_post, name='send_post'),
    path('edit_post<int:post_id>/', views.edit_post, name='edit_post'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
