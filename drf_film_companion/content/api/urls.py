from django.urls import path
from content.api.views_json import movie_list, movie_details
from content.api.views import movies_serialized_list, movie_serialized_details

urlpatterns = [
    path('json/', movie_list, name='movie-list'),
    path('json/<int:pk>', movie_details, name='movie-details'),
    path('list/', movies_serialized_list, name='movies_serialized_list'),
    path('list/<int:pk>', movie_serialized_details, name='movie_serialized_details'),
]