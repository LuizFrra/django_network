from django.core.exceptions import ValidationError
from django.test import TestCase
from network.models import Post
from datetime import datetime


class TestPostModel(TestCase):
    def test_given_valid_data_when_creating_post_then_saves_successfully(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Valid Title",
            "content": "Valid Content"
        }

        # When
        post = Post(**data)
        post.full_clean()  # Validates model fields
        post.save()

        # Then
        self.assertIsInstance(post, Post)
        self.assertEqual(post.username, data["username"])
        self.assertEqual(post.title, data["title"])
        self.assertEqual(post.content, data["content"])
        self.assertIsNotNone(post.created_datetime)

    def test_given_missing_username_when_creating_post_then_raises_validation_error(self):
        # Given
        post = Post(title="Valid Title", content="Valid Content")

        # When / Then
        with self.assertRaises(ValidationError):
            post.full_clean()  # Validate model fields before saving

    def test_given_missing_title_when_creating_post_then_raises_validation_error(self):
        # Given
        post = Post(username="test_user", content="Valid Content")

        # When / Then
        with self.assertRaises(ValidationError):
            post.full_clean()  # Validate model fields before saving

    def test_given_missing_content_when_creating_post_then_raises_validation_error(self):
        # Given
        post = Post(username="test_user", title="Valid Title")

        # When / Then
        with self.assertRaises(ValidationError):
            post.full_clean()  # Validate model fields before saving

    def test_given_valid_post_when_updating_then_saves_changes(self):
        # Given
        post = Post.objects.create(
            username="test_user",
            title="Original Title",
            content="Original Content"
        )

        # When
        post.title = "Updated Title"
        post.content = "Updated Content"
        post.full_clean()  # Validate model fields before saving
        post.save()

        # Then
        updated_post = Post.objects.get(id=post.id)
        self.assertEqual(updated_post.title, "Updated Title")
        self.assertEqual(updated_post.content, "Updated Content")

    def test_given_long_username_when_creating_post_then_raises_validation_error(self):
        # Given
        post = Post(username="a" * 65, title="Valid Title", content="Valid Content")

        # When / Then
        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_given_long_title_when_creating_post_then_raises_validation_error(self):
        # Given
        post = Post(username="test_user", title="a" * 129, content="Valid Content")

        # When / Then
        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_given_no_created_datetime_when_creating_post_then_auto_populates(self):
        # Given
        data = {
            "username": "test_user",
            "title": "Valid Title",
            "content": "Valid Content"
        }

        # When
        post = Post(**data)
        post.full_clean()
        post.save()

        # Then
        self.assertIsInstance(post.created_datetime, datetime)
