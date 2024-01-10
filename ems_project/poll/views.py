from django.shortcuts import render
from poll.models import Question, Choice


# Create your views here.
def poll_list(request):
    context = {"title": "poll"}
    questions = Question.objects.all()
    context["questions"] = questions
    return render(request, "poll/index.html", context)


def poll_detail(request, id: int):
    context = {"title": "poll"}
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        questions = None
    context["question"] = question
    return render(request, "poll/detail.html", context)
