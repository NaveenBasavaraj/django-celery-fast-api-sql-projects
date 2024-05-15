from rest_framework import serializers
from content.models import Movie

class MovieSerializer(serializers.Serializer):
    # get or validate
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    # post
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # put
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance
