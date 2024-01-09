from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'employee'
    }
    render(request, 'employee/index.html', context)