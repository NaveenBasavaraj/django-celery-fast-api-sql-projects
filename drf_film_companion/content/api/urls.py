from django.urls import path
from content.api.views_json import movie_list, movie_details
from drf_film_companion.content.api.views_function import movies_serialized_list, movie_serialized_details

urlpatterns = [
    path('json/list', movie_list, name='movie-list'),
    path('json/list/<int:pk>', movie_details, name='movie-details'),
    path('func/list', movies_serialized_list, name='movies_serialized_list'),
    path('func/list/<int:pk>', movie_serialized_details, name='movie_serialized_details'),
]