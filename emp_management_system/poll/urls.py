from django.urls import path
from poll.views import *

app_name = "poll"
urlpatterns = [
    path("", index, name="index"),
    path("<int:id>/detail/", details, name="details"),
    path("<int:id>/", poll_page, name="poll_page"),
]
