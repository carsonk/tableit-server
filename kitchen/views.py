from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import MenuItem, Order
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

def index(request):
    page = "<html><head><title>Recent Orders</title></head><body>"

    recent_orders = Order.objects.all().order_by('-time_submitted')

    for order in recent_orders:
        total_price = 0
        print(order)
        page += "<div><em>Ordered %s</em><ol>" % order.time_submitted.isoformat()

        menu_items = order.menu_items.all()
        for item in menu_items:
            page += "<li>%s - $%d</li>" % (item.title, item.price)
            total_price += item.price

        page += "</ol>Total: <strong>$%d</strong></div><br />" % total_price

    page += "</body></html>"

    return HttpResponse(page)

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
