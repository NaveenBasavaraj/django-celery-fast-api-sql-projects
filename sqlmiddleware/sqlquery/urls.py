from django.urls import path
from sqlquery.views import home

urlpatterns = [
    path("", home, name="home"),
]
