from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('shope',views.shope,name='shope'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    # path('update_item/', views.updateItem, name="update_item"),
	# path('process_order/', views.processOrder, name="process_order"),
]
