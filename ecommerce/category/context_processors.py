""" 
It tales a request as an argument and it will return
the dictionary of data as a context.

In below function we are going to fetch all the 
categories from the database

note:
By adding menu_links inside settings.py we can add it into any template as want"""


from .models import Category

def menu_links(request):
    links=Category.objects.all() #Query list
    return dict(links=links)