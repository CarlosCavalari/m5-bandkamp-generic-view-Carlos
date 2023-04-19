from rest_framework import serializers
from .models import Album

 
class AlbumSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
    
    class Meta:
        model = Album
        exclude = [
            "user"
        ]
