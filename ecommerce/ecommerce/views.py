from django.shortcuts import render

from store.models import Product



def home(request):
    product=Product.objects.all
    context={
        'products':product
    }
    return render(request,'home.html',context)