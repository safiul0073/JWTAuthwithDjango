from django.urls import path
from .views import RegisterAPI, LoginAPI

urlpatterns = [
    # path('login/', views.lognView, name='login'),
    # path('register/', views.CreateUserView, name='register'),
    # path('messages', views.getAllMessages, name='messages')
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
]