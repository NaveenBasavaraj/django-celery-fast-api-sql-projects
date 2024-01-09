from django.urls import path
from poll.views import index

app_name = 'Poll'
urlpatterns = [
    path('', index, name='index'),
]