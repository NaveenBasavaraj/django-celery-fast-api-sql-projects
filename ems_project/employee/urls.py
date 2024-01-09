from django.urls import path
from employee.views import index

app_name = 'Employee'
urlpatterns = [
    path('', index, name='index'),
]