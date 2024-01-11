from django.urls import path
from employee.views import *

app_name = 'Employee'
urlpatterns = [
    # Create
    path('add/', employee_add, name="employee_add"),
    # Retreive
    path('list/', employee_list, name='employee_list'),
    path('<int:id>', employee_details, name="employee_details"),
    # Update
    path('<int:id>/edit', employee_edit, name="employee_edit"),
    # Delete
    path('<int:id>/delete/', employee_delete, name="employee_delete")
]