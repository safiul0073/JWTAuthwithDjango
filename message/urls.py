from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverView, name='api_overview'),
    path('messages/<int:pk>', views.MessageListView, name='messages'),
    path('messages', views.getAllMessages, name='messages')
]