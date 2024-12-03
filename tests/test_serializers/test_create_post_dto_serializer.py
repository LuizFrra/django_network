from django.test import TestCase

from network.serializers.create_post_dto_serializer import CreatePostDTOSerializer


class TestCreatePostDTOSerializer(TestCase):

    def test_given_valid_data_when_validating_then_serializer_is_valid(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Valid Title",
            "content": "This is valid content."
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is True
        assert serializer.validated_data == data

    def test_given_short_username_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "usr",
            "title": "Valid Title",
            "content": "This is valid content."
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "username" in serializer.errors
        assert serializer.errors["username"][0] == "Ensure this field has at least 4 characters."

    def test_given_short_title_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Tit",
            "content": "This is valid content."
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "title" in serializer.errors
        assert serializer.errors["title"][0] == "Ensure this field has at least 4 characters."

    def test_given_short_content_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Valid Title",
            "content": "Con"
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "content" in serializer.errors
        assert serializer.errors["content"][0] == "Ensure this field has at least 4 characters."

    def test_given_username_exceeds_max_length_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "a" * 65,
            "title": "Valid Title",
            "content": "This is valid content."
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "username" in serializer.errors
        assert serializer.errors["username"][0] == "Ensure this field has no more than 64 characters."

    def test_given_title_exceeds_max_length_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "test_user",
            "title": "a" * 129,
            "content": "This is valid content."
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "title" in serializer.errors
        assert serializer.errors["title"][0] == "Ensure this field has no more than 128 characters."

    def test_given_content_exceeds_max_length_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Valid Title",
            "content": "a" * 513
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "content" in serializer.errors
        assert serializer.errors["content"][0] == "Ensure this field has no more than 512 characters."

    def test_given_missing_content_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Valid Title"
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "content" in serializer.errors
        assert serializer.errors["content"][0] == "This field is required."

    def test_given_missing_username_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "title": "Valid Title",
            "content": "This is valid content."
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "username" in serializer.errors
        assert serializer.errors["username"][0] == "This field is required."

    def test_given_missing_title_when_validating_then_serializer_raises_error(self):
        # Given
        data = {
            "username": "test_user",
            "content": "This is valid content."
        }

        # When
        serializer = CreatePostDTOSerializer(data=data)

        # Then
        assert serializer.is_valid() is False
        assert "title" in serializer.errors
        assert serializer.errors["title"][0] == "This field is required."
