from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    return render(request, "accounts/login.html")

def register(request):
    return render(request, "accounts/register.html")

def product(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {'products': products})

def category(request):
    return render(request, "accounts/category.html")
