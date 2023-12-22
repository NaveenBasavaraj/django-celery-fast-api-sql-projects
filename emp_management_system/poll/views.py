from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"title": "polls"}
    return render(request, "poll/index.html", context)
