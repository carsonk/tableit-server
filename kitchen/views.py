from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import MenuCategory, MenuItem

def index(request):
    return HttpResponse("Hello, world!")

def menu(request):
    menu = list(MenuItem.objects.all().values())
    return JsonResponse(menu, safe=False)
