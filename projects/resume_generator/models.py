from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField()
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    pre_work = models.TextField()
    skills = models.TextField()

    def __str__(self) -> str:
        return self.name
