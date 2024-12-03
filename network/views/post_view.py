from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from network.models import Post
from network.serializers.create_post_dto_serializer import CreatePostDTOSerializer
from network.serializers.post_dto_serializer import PostDTOSerializer
from network.serializers.update_post_dto_serializer import UpdatePostDTOSerializer


class PostPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 100


class PostView(GenericAPIView):
    serializer_class = PostDTOSerializer
    pagination_class = PostPagination

    @staticmethod
    def post(request):
        serializer = CreatePostDTOSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        post = Post.objects.create(**data)
        res = PostDTOSerializer(post)

        return Response(
            res.data,
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @staticmethod
    def patch(request, post_id):
        post = post = get_object_or_404(Post, id=post_id)

        serializer = UpdatePostDTOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data
        post.title = validated_data['title']
        post.content = validated_data['content']
        post.save()

        res = PostDTOSerializer(post)
        return Response(res.data, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return Post.objects.all().order_by('-created_datetime')
