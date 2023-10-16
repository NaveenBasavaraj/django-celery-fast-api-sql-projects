from django.urls import path
from users.views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='user_login'),
    path('logout/', auth_view.LogoutView.as_view(template_name="users/logout.html"), name='user_logout'),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name="users/password_change.html"), name='password_change'),
]
