from rest_framework import serializers


class CreatePostDTOSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64, min_length=4)
    title = serializers.CharField(max_length=128, min_length=4)
    content = serializers.CharField(max_length=512, min_length=4)
