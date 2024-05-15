from content.models import Movie
from content.api.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def movies_serialized_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serialized_movies = MovieSerializer(movies, many=True)
        return Response(serialized_movies.data)
    
    if request.method == 'POST':
        movie_data = MovieSerializer(data=request.data)
        if movie_data.is_valid():
            movie_data.save()
            return Response(movie_data.data, status=status.HTTP_201_CREATED)
        return Response(movie_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_serialized_details(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialized_movie = MovieSerializer(movie)
        return Response(serialized_movie.data)
    
    if request.method == 'PUT':
        updated_movie_data = MovieSerializer(movie, data=request.data)
        if updated_movie_data.is_valid():
            updated_movie_data.save()
            return Response(updated_movie_data.data)
        return Response(updated_movie_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
