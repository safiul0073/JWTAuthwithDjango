from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('product/', views.product),
    path('category/', views.category),
]