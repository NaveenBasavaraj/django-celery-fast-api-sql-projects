from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.urls import reverse
from employee.forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
 
def user_login(request):
    context = {}
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse("user_success"))
        else:
            context["error"] = "provide valid credentials"
            return render(request, 'auth/login.html', context)
    else:
        return render(request, 'auth/login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url="/login/")
def success(request):
    context = {}
    context["user"] = request.user
    return render(request, "auth/success.html", context)

@login_required(login_url="/login/")
def employee_list(request):
    context = {
        "title":"Employees",
        "users": User.objects.all()
    }
    return render(request, 'employee/index.html', context)

@login_required(login_url="/login/")
def employee_details(request,id=None):
    context = {
        "title":"employee details",
        "user": get_object_or_404(User, id=id)
    }
    return render(request, 'employee/details.html', context)

@login_required(login_url="/login/")
def employee_add(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', {"user_form": user_form})
    else:
        user_form = UserForm()
        return render(request, 'employee/add.html',  {"user_form":user_form})
        
@login_required(login_url="/login/")
def employee_edit(request,id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/edit.html', {"user_form": user_form})
    else:
        user_form = UserForm()
        return render(request, 'employee/edit.html', {"user_form": user_form})

@login_required(login_url="/login/")
def employee_delete(request,id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {
            'user':user
        }
        return render(request, 'employee/delete.html', context)
