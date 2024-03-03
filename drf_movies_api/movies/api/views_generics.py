from movies.models import Movie, Stream, Review
from movies.api.serializers import MovieSerializer, ReviewSerializer, SteamSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, mixins

class MovieList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MovieDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, 
                   mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StreamList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Stream.objects.all()
    serializer_class = SteamSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StreamDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, 
                   mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Stream.objects.all()
    serializer_class = SteamSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReviewDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, 
                   mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)