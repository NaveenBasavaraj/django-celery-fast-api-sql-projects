from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    @property
    def choices(self):
        return self.choice_set.all()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.choice
    
    @property
    def votes(self):
        return self.answer_set.count()
    
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    create_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.choice.choice
    