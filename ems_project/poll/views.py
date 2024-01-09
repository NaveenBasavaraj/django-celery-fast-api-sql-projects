from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'poll'
    }
    render(request, 'poll/index.html', context)