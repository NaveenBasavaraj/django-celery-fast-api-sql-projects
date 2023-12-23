from django.shortcuts import render, redirect, get_object_or_404
from poll.models import Question, Choice, Answer

# Create your views here.


def index(request):
    questions = Question.objects.all()
    context = {
        "title": "polls",
        "questions": questions,
    }
    return render(request, "poll/index.html", context)


def details(request, id):
    question = Question.objects.get(id=id)
    context = {"title": "polls", "question": question}
    return render(request, "poll/details.html", context)


def poll_page(request, id):
    if request.method == "GET":
        question = Question.objects.get(id=id)
        context = {"title": "polls", "question": question}
        return render(request, "poll/poll.html", context)

    if request.method == "POST" and request.user and request.user.is_authenticated:
        print(request.POST.get("answer"))
        answer_id = request.POST.get("answer")
        choice = get_object_or_404(Choice, pk=answer_id)
        if choice:
            ret = Answer.objects.create(user=request.user, choice=choice)
            if ret:
                return redirect("poll:details", id=id)
        return render(request, "poll/poll.html", context)
