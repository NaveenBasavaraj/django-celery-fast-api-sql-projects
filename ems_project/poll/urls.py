from django.urls import path
from poll.views import poll_list, poll_detail

app_name = "Poll"
urlpatterns = [
    path("", poll_list, name="poll-list"),
    path("detail/<int:id>", poll_detail, name="poll-detail"),
]
