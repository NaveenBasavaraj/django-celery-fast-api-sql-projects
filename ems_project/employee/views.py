from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from employee.forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            url = reverse("Employee:employee_list")
            return HttpResponseRedirect(url)
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    return render(request, "auth/login.html", context)


def user_logout(request):
    context = {}
    if request.method == "POST":
        logout(request)
        return render(request, "auth/login.html", context)


def success(request):
    context = {
        "user": request.user,
    }
    return render(request, "auth/success.html", context)


def employee_list(request):
    context = {"title": "employee", "users": User.objects.all()}
    return render(request, "employee/index.html", context)


def employee_add(request):
    user_form = UserForm()
    context = {"user_form": user_form}
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            url = reverse("employee_list")
            return HttpResponseRedirect(url)
        context["user_form"] = user_form
        return render(request, "employee/add.html", context)

    return render(request, "employee/add.html", context)


def employee_details(request, id: int):
    context = {"title": "employee", "users": get_list_or_404(User, id=id)}
    return render(request, "employee/details.html", context)


def employee_edit(request, id: int):
    user = get_list_or_404(User, id=id)
    user_form = UserForm(instance=user)
    context = {"user_form": user_form}
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            url = reverse("employee_list")
            return HttpResponseRedirect(url)
        context["user_form"] = user_form
        return render(request, "employee/edit.html", context)
    return render(request, "employee/edit.html", context)


def employee_delete(request, id: int):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        url = reverse("employee_list")
        return HttpResponseRedirect(url)
    else:
        context = {}
        context["user"] = user
        return render(request, "employee/delete.html", context)
