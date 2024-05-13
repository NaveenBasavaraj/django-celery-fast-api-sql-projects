from django.shortcuts import render, get_object_or_404
from employee.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from employee.forms import UserForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    profiles = Profile.objects.all()
    context = {
        "page":"employee",
        "profiles": profiles,
    }
    return render(request, "employee/index.html", context)

def details(request, id=None):
    profile = get_object_or_404(Profile, id=id)
    print(profile)
    print(profile.user.first_name, profile.user.last_name, profile.user.username, profile.user.email)
    context = {
        "page":"profile",
        "profiles": profile,
    }
    return render(request, "employee/details.html", context)

def employee_add(request):
    if request.method == "POST":
        print("hereee")
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/employee/')
        else:
            return render(request, 'employee/add.html', {"user_form":user_form})
    else:
        user_form = UserForm()
        return render(request, 'employee/add.html', {"user_form":user_form})
    
def employee_edit(request, id=None):
    user = get_object_or_404(User,id=id)
    if request.method == "POST":
        print("hereee")
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/employee/')
        else:
            return render(request, 'employee/edit.html', {"user_form":user_form})
    else:
        user_form = UserForm()
        return render(request, 'employee/edit.html', {"user_form":user_form})

def employee_delete(request, id=None):
    user = get_object_or_404(User,id=id)
    user.delete()
    return HttpResponseRedirect('/employee/')

def user_login(request):
    context = {}
    if request.method == "POST":
        pass
    else:
        return render(request, "auth/login.html", context)

def user_logout(request):
    pass

def success(request):
    pass