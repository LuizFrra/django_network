from datetime import datetime
from django.test import TestCase

from django.utils.timezone import make_aware

from network.serializers.post_dto_serializer import PostDTOSerializer


class TestPostDTOSerializer(TestCase):

    def test_given_valid_data_when_validating_then_serializer_is_valid(self):
        # Given
        data = {
            "id": 1,
            "username": "test_user",
            "title": "Valid Title",
            "content": "This is valid content.",
            "created_datetime": make_aware(datetime.now())
        }

        # When
        serializer = PostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is True
        assert serializer.validated_data == data

    def test_given_missing_id_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Valid Title",
            "content": "This is valid content.",
            "created_datetime": make_aware(datetime.now())
        }

        # When
        serializer = PostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "id" in serializer.errors
        assert serializer.errors["id"][0] == "This field is required."

    def test_given_invalid_username_length_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "id": 1,
            "username": "a" * 33,
            "title": "Valid Title",
            "content": "This is valid content.",
            "created_datetime": make_aware(datetime.now())
        }

        # When
        serializer = PostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "username" in serializer.errors
        assert serializer.errors["username"][0] == "Ensure this field has no more than 32 characters."

    def test_given_missing_title_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "id": 1,
            "username": "test_user",
            "content": "This is valid content.",
            "created_datetime": make_aware(datetime.now())
        }

        # When
        serializer = PostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "title" in serializer.errors
        assert serializer.errors["title"][0] == "This field is required."

    def test_given_invalid_content_length_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "id": 1,
            "username": "test_user",
            "title": "Valid Title",
            "content": "a" * 513,
            "created_datetime": make_aware(datetime.now())
        }

        # When
        serializer = PostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "content" in serializer.errors
        assert serializer.errors["content"][0] == "Ensure this field has no more than 512 characters."

    def test_given_invalid_created_datetime_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "id": 1,
            "username": "test_user",
            "title": "Valid Title",
            "content": "This is valid content.",
            "created_datetime": "invalid_date"
        }

        # When
        serializer = PostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "created_datetime" in serializer.errors
        assert serializer.errors["created_datetime"][
                   0] == "Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
