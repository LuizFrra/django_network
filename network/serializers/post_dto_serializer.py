from rest_framework import serializers


class PostDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=32)
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=512)
    created_datetime = serializers.DateTimeField()
