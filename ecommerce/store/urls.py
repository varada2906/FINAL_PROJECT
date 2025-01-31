
from django.urls import path,include

from .import views

urlpatterns = [
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.product_detail,name='product_detail')   
]
#http://127.0.0.0.1.8000/store/t-shirts
#http://127.0.0.0.1.8000/store/t-shirts/tshirt
