from rest_framework import serializers


class UpdatePostDTOSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128, min_length=4)
    content = serializers.CharField(max_length=512, min_length=4)
