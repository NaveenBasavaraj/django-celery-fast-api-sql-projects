from django.urls import path
from movies.api.views_apiclass import (MovieList, StreamList, ReviewList, 
                              MovieDetails, StreamDetails, ReviewDetails)

urlpatterns = [
    path('MovieList/', MovieList.as_view(), name='MovieList'),
    path('StreamList/', StreamList.as_view(), name='StreamList'),
    path('ReviewList/', ReviewList.as_view(), name='ReviewList'),
    path('MovieList/<int:id>/', MovieDetails.as_view(), name='MovieDtls'),
    path('StreamList/<int:id>/', StreamDetails.as_view(), name='StreamDtls'),
    path('ReviewList/<int:id>/', ReviewDetails.as_view(), name='ReviewDtls'),
]