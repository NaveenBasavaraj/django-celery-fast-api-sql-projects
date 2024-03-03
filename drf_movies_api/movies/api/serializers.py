from rest_framework import serializers
from movies.models import Movie, Stream, Review

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    storyline = serializers.CharField()
    active = serializers.BooleanField()
    #stream = serializers.CharField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.name)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField()
    description = serializers.CharField()
    #movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    
    def create(self, validated_data):
        return Review.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.description = validated_data.get('description', instance.description)
        return instance
    
class SteamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    about = serializers.CharField()
    website = serializers.CharField()
    
    def create(self, validated_data):
        return Stream.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        return instance