from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import MenuItem, Order
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Hello, world!")

def menu(request):
    menu = list(MenuItem.objects.all().values())
    return JsonResponse(menu, safe=False)

@csrf_exempt
def order(request):
    return_val = {'success': False}
    received_data = json.loads(request.body.decode("UTF-8"))
    new_order = Order()
    new_order.save()

    if 'orders' not in received_data:
        return JsonResponse(return_val)

    for order_id in received_data['orders']:
        new_order.menu_items.add(order_id)

    return_val['success'] = True
    return JsonResponse(return_val)
