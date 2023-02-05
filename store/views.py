from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
# from .models import *
# from .utils import cookieCart, cartData, guestOrder
from .models import Product

# Create your views here.
def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store.html',context=context)

def home(request):
    return render(request,'index.html')
def cart(request):
    context={}
    return render(request,'cart.html',context=context)

def checkout(request):
    context={}
    return render(request,'checkout.html',context=context)
