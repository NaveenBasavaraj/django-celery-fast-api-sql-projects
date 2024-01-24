from django.http import HttpResponse
from django.shortcuts import render
from email_app.forms import ReviewForm
from django.views.generic.edit import FormView


class ReviewEmailView(FormView):
    template_name = "review.html"
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!!"
        return HttpResponse(msg)
