from django.urls import path
from employee.views import index, details, employee_add, employee_edit, employee_delete

app_name="employee_app"
urlpatterns = [
    path('', index, name="employees-list"),
    path('<int:id>/details', details, name="employee-details"),
    path('<int:id>/edit', employee_edit, name='employee-edit'),
    path('add/', employee_add, name='employee-add'),
    path('<int:id>/delete', employee_delete, name='employee-delete'),
]