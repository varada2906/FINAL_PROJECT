from django.shortcuts import render

# Create your views here.
from .models import Product

def store(request):
    products=Product.oblects.all()
    product_count=products.count()
    context={
        'products':products,
        'product_count':product_count
    }
    return render(request,'store/store.html',context)















from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
#Create your views here.

#get post put patch
def store(request,category_slug=None):
    categories=None
    products=None

    if category_slug!=None:
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
        product_count=products.count()
    else:
        products=Product.object.all().filter(is_available=True)
        product_count=products.count()
    context={
        'products':products,
        'products_count':product_count
    }
    return render(request,'store/store.html',context)
''' 
Logic:
->Whenever the user request for any categories ,for example lets take shirts
example URL:127.0.0.1:8000/shirts/
->Then the user should able to see all the products that belongs to the particular category.
->The last part/shirts/ is basically the slug
->firstly we will create a url pattern 
->inside store method or store view we have to accept the category_slug
->if there is nothing in the slug (if category_slug!=None :)then
we should do all the database operations
->get_object_or_404 bring the categories if found or will return the 404 error
'''
def product_detail(request,category_slug,product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug,slug =product_slug)
    except Exception as e:
        raise e
    context={
        'single_product':single_product
    }
    return  render(request,'store/product_detail.html',context)
