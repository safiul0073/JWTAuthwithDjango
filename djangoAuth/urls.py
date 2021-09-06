import accounts
from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from accounts import views




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('message.urls')),
    path('', include('accounts.urls')),
    path('', include('apiAuth.urls')),
]
