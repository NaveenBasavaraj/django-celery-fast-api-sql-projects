from django.shortcuts import render
from poll.models import Question, Choice, Answer
from django.http import Http404 
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        "page":"poll",
        "questions":questions
    }
    return render(request, "poll/index.html", context)

def details(request, id):
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context = {
        "page":"poll details",
        "question":question
    }
    if request.method == "GET":
        return render(request, "poll/details.html", context)
    
    if request.method == "POST":
        print("its here")
        user = user = request.user.id
        data = request.POST
        print(data)
        if user and data:
            ret = Answer.objects.create(user_id=user, choice_id=data['answer'])
        return render(request, "poll/details.html", context)

def poll(request, id):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {
            "page":"poll",
            "question":question
        }
        return render(request, "poll/poll.html", context)