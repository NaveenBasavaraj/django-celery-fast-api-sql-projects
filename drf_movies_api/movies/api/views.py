from movies.models import Movie, Stream, Review
from movies.api.serializers import MovieSerializer, ReviewSerializer, SteamSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Function Based Views
@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serialzer = MovieSerializer(movies, many=True)
        return Response(serialzer.data)
    if request.method == 'POST':
        serialzer = MovieSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data)

@api_view(["GET", "PUT", "DELETE"])
def movie_details(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serialzer = MovieSerializer(movie)
        return Response(serialzer.data)
    
    if request.method == 'PUT':
        serialzer = MovieSerializer(movie, request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        movie.delete()
        return Response(serialzer.data, status=status.HTTP_200_OK)
    
@api_view(["GET", "POST"])
def stream_list(request):
    if request.method == 'GET':
        streams = Stream.objects.all()
        serialzer = SteamSerializer(streams, many=True)
        return Response(serialzer.data)
    if request.method == 'POST':
        serialzer = SteamSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def stream_details(request, id):
    try:
        stream = Stream.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serialzer = SteamSerializer(stream)
        return Response(serialzer.data)
    
    if request.method == 'PUT':
        serialzer = SteamSerializer(stream, request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        stream.delete()
        return Response(serialzer.data, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serialzer = ReviewSerializer(reviews, many=True)
        return Response(serialzer.data)
    if request.method == 'POST':
        serialzer = ReviewSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def review_details(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serialzer = ReviewSerializer(review)
        return Response(serialzer.data)
    
    if request.method == 'PUT':
        serialzer = ReviewSerializer(review, request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialzer.data, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        review.delete()
        return Response(serialzer.data, status=status.HTTP_200_OK)


# Class Based Views