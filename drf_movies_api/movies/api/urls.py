from django.urls import path
from movies.api.views import (movie_list, stream_list, review_list, 
                              movie_details, stream_details, review_details)

urlpatterns = [
    path('movie_list/', movie_list, name='movie_list'),
    path('stream_list/', stream_list, name='stream_list'),
    path('review_list/', review_list, name='review_list'),
    path('movie_list/<int:id>/', movie_details, name='movie_dtls'),
    path('stream_list/<int:id>/', stream_details, name='stream_dtls'),
    path('review_list/<int:id>/', review_details, name='review_dtls'),
]
