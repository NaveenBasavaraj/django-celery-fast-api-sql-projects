from django.urls import path
from poll.views import index, details

app_name = 'Poll'
urlpatterns = [
    path('', index, name='polls'),
    path('<int:id>/details', details, name='details'),
]
