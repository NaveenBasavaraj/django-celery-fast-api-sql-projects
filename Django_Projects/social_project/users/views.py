from django.shortcuts import render
from users.forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def user_login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            authenticated_user_obj = authenticate(request, username=data['username'], password=data['password'])
            if authenticated_user_obj:
                login(request, authenticated_user_obj)
                #return render(request, 'users/main.html')
                return HttpResponse("User Authenticated")
            else:
                return HttpResponse("Invalid User")

    form = LoginForm()
    return render(request,'users/login.html',{'form':form})

