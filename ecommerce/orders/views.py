from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse
from carts.models import CartItem
from.forms import OrderForm
from .models import Order,Payment,OrderProduct
import json
from store.models import Product
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def payments(request):
    body=json.loads(request.body)
    order=Order.objects.get(user=request.user,is_ordered=False,order_number=body['orderID'])
    #Store transaction details inside payment model
    payment=Payment(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=order.order_total,
        status=body['status'],
    )
    payment.save()

    order.payment=payment
    order.is_ordered=True
    order.save()


#move the cart items to order product table
cart_items=CartItem.objects.filter(user=request.user)

for item in cart_items:
    orderproduct=OrderProduct()
    orderproduct.order_id=order.id
    orderproduct.payment=payment
    orderproduct.user_id=request.user.id
    orderproduct.product_id=item.product_id
    orderproduct.quantity=item.quantity
    orderproduct.product_price=item.product.price
    orderproduct.ordered=True
    orderproduct.save()
    

    