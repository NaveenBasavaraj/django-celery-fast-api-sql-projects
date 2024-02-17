from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from poll.models import Question, Choice, Answer
from django.urls import reverse
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
    
    if request.method == "POST":
        user_id = 1
        data = request.POST
        ret = Answer.objects.create(user_id=user_id, choice_id=data["answer"])
        if ret:
            return HttpResponse("Your vote is done")
            # url = ''
            # return redirect(reverse(url))
        else:
            return HttpResponse("Your vote is NOT done")