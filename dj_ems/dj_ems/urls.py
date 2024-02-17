"""
URL configuration for dj_ems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from employee.views import user_login, success, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('poll/', include('poll.urls')),
    path('emp/', include('employee.urls')),
    path('login/', user_login, name="user_login"),
    path('poll/', success, name="user_success"),
    path('emp/', user_logout, name="user_logout"),
]
