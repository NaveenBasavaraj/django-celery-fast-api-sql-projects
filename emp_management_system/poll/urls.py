from django.urls import path
from poll.views import *

app_name = "poll"
urlpatterns = [
    path("", index, name="index"),
]
