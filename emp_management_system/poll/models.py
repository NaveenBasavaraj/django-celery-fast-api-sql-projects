from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    poll_start_date = models.DateTimeField(null=True, blank=True)
    poll_end_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=50)
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice

    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + "-" + self.choice.text
