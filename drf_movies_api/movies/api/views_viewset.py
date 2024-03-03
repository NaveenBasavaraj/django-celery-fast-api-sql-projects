from movies.models import Movie, Stream, Review
from movies.api.serializers import MovieSerializer, ReviewSerializer, SteamSerializer
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets

