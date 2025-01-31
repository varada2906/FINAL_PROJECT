from django.shortcuts import render

# Create your views here.
# Business logic

# 9 pm okay 

from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required




# business logic in our views.py of the accounts app

# http://127.0.0.1:8000/accounts/logout
def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email'] # rani@gmail.com
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request,'Registration successfull')
            return redirect('register') # dynamic routing
    else:
        print("i am here")
        form = RegistrationForm() # empty form render get request
    context = {
        'form': form,#dictionary form
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password) # None

        if user is not None:
            auth.login(request,user)
            return redirect('login')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('register')
    return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
