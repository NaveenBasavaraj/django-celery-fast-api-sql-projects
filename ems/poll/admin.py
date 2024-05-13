from django.contrib import admin
from poll.models import Question, Choice, Answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
