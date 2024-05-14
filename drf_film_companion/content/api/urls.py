from django.urls import path
from content.api.views_json import movie_list, movie_details

urlpatterns = [
    path('json/', movie_list, name='movie-list'),
    path('json/<int:pk>', movie_details, name='movie-details'),
]