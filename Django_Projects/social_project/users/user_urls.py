from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('login/',user_login, name='user_login'),
    path('logout/',LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
