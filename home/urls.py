from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('add_post/', views.add_post, name='add_post'),
]