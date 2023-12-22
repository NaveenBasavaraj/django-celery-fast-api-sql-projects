from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)
    salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def auto_create_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, "profile"):
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
