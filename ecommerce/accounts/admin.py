from django.contrib import admin

# Register your models here.
from .models import Account,UserProfile

admin.site.register(Account)
admin.site.register(UserProfile)