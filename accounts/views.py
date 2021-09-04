from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'main/dashboard.html')

def login(request):
    return HttpResponse("login")

def register(request):
    return HttpResponse("register")

def product(request):
    return HttpResponse("product")

def category(request):
    return HttpResponse("category")
