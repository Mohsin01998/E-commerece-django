from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
# from .models import *
# from .utils import cookieCart, cartData, guestOrder

# Create your views here.
def shope(request):
    context={}
    return render(request,'shope.html',context=context)

def home(request):
    return render(request,'index.html')
def cart(request):
    context={}
    return render(request,'cart.html',context=context)

def checkout(request):
    context={}
    return render(request,'checkout.html',context=context)
