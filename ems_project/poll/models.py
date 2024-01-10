from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=50, null=False, blank=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.question

    @property
    def choice_set(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=25, null=False)
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Q" + str(self.question.id) + " : " + self.choice

    @property
    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "U" + str(self.user.id) + " : " + str(self.choice.id)
