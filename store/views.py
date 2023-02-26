from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import Product, Order, OrderItem, ShippingAddress
import joblib
import random




def getBotResponse(request):
    responses = joblib.load("labelencoder/ecomresponses.pkl")
    vectorizer = joblib.load("vectorizer/ecomtext_vectorizer.pkl")
    model = joblib.load("model/ecomchatbot_model.pkl")
    le = joblib.load("labelencoder/ecomle.pkl")
    # usertext =  request.args.get('msg')
    chat = []
    usertext = request.GET['msg']
    chat.append(usertext)
    # chat = pd.Series(usertext)
    X_test_dtm1 = vectorizer.transform(chat)
    y_pred_class1 = model.predict(X_test_dtm1)
    z = le.inverse_transform([y_pred_class1[0]])
    reply = random.choice(responses[z[0]][0])
    return JsonResponse(reply,safe=False)
def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total=float(data['form']['total'])
        order.transaction_id=transaction_id
        if total==order.get_cart_total:
            order.complete=True
        order.save()

        if order.shipping==True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print("User is not logged in..")
    return JsonResponse("Payment subbmitted..",safe=False)


def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action = data['action']
    print("action:",action)
    print("productId:",productId)
    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created=OrderItem.objects.get_or_create(order=order, product=product)
    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems=order['get_cart_items']

    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store.html',context=context)

def home(request):
    return render(request,'index.html')
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0, 'shipping':False}
        cartItems=order['get_cart_items']
    context={'items':items, 'order':order,'cartItems':cartItems}
    return render(request,'cart.html',context=context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request,'checkout.html',context=context)
