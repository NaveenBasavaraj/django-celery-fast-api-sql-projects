from django.urls import path
from poll.views import index, details, poll

app_name="poll_app"
urlpatterns = [
    path('', index, name="polls-list"),
    path('<int:id>', poll, name='poll-vote'),
    path('<int:id>/results', details, name="poll-details"),
]