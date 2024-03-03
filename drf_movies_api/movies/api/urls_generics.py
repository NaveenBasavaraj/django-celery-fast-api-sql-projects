from django.urls import path
from movies.api.views_generics import (MovieList, StreamList, ReviewList, 
                              MovieDetail, StreamDetail, ReviewDetail)

urlpatterns = [
    path('movie_list/', MovieList.as_view(), name='MovieList'),
    path('stream_list/', StreamList.as_view(), name='StreamList'),
    path('review_list/', ReviewList.as_view(), name='ReviewList'),
    path('movie_list/<int:pk>/', MovieDetail.as_view(), name='MovieDetail'),
    path('stream_list/<int:pk>/', StreamDetail.as_view(), name='StreamDetail'),
    path('review_list/<int:pk>/', ReviewDetail.as_view(), name='ReviewDetail'),
]