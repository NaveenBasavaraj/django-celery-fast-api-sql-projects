from django.shortcuts import render
from django.http import Http404
from poll.models import Question, Choice
# Create your views here.

def index(request):
    context = {
        "questions":Question.objects.all(),
        "title":"Polls"
    }
    return render(request, 'poll/index.html', context)

def details(request, id):
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context = {
        "question":question,
        "title":"details"
    }
    return render(request, 'poll/detail.html', context)

def poll(request, id=None):
    if request.method == 'GET':
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {
            "question":question,
            "title":"poll"
        }
        return render(request, 'poll/poll.html', context)