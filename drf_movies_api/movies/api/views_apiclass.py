from movies.models import Movie, Stream, Review
from movies.api.serializers import MovieSerializer, ReviewSerializer, SteamSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# class based views

class MovieList(APIView):
    '''
    takes GET and PUT request
    '''
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetails(APIView):
    '''
    takes GET, PUT, DELETE
    '''
    def get(self, request, id):
        try:
            movie = Movie.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        try:
            movie = Movie.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(instance=movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request):
        try:
            movie = Movie.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamList(APIView):
    '''
    takes GET and PUT request
    '''
    def get(self, request):
        streams = Stream.objects.all()
        serializer = SteamSerializer(streams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SteamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamDetails(APIView):
    '''
    takes GET, PUT, DELETE
    '''
    def get(self, request, id):
        try:
            stream = Stream.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SteamSerializer(stream)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        try:
            stream = Stream.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SteamSerializer(instance=stream)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request):
        try:
            stream = Stream.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ReviewList(APIView):
    '''
    takes GET and PUT request
    '''
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetails(APIView):
    '''
    takes GET, PUT, DELETE
    '''
    def get(self, request, id):
        try:
            review = Review.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        try:
            review = Review.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(instance=review)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request):
        try:
            review = Review.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



