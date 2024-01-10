from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"title": "employee"}
    return render(request, "employee/index.html", context)
