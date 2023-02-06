from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
# from .models import *
# from .utils import cookieCart, cartData, guestOrder
from .models import Product, Order

# Create your views here.
def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store.html',context=context)

def home(request):
    return render(request,'index.html')
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
    context={'items':items, 'order':order}
    return render(request,'cart.html',context=context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request,'checkout.html',context=context)
