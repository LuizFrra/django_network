from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from network.models import Post


class TestPostView(TestCase):
    def setUp(self):
        # Every test initializes its own client
        self.client = APIClient()

    def test_given_valid_data_when_posting_then_creates_post(self):
        # Given
        data = {
            "username": "new_user",
            "title": "New Title",
            "content": "New Content"
        }

        # When
        response = self.client.post("/careers/", data)

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], data["username"])
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["content"], data["content"])
        self.assertTrue(Post.objects.filter(username="new_user", title="New Title").exists())

    def test_given_posts_when_getting_then_returns_posts(self):
        # Given
        post1 = Post.objects.create(username="test_user1", title="Title 1", content="Content 1")

        # When
        response = self.client.get("/careers/")

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertGreater(len(response.data["results"]), 0)
        self.assertEqual(response.data["results"][0]["title"], post1.title)  # Ordered by created_datetime

    def test_given_valid_data_when_patching_then_updates_post(self):
        # Given
        post = Post.objects.create(username="test_user", title="Old Title", content="Old Content")
        data = {
            "title": "Updated Title",
            "content": "Updated Content"
        }

        # When
        response = self.client.patch(f"/careers/{post.id}/", data)

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["content"], data["content"])
        post.refresh_from_db()
        self.assertEqual(post.title, "Updated Title")
        self.assertEqual(post.content, "Updated Content")

    def test_given_existing_post_when_deleting_then_removes_post(self):
        # Given
        post = Post.objects.create(username="test_user", title="Title to Delete", content="Content to Delete")

        # When
        response = self.client.delete(f"/careers/{post.id}/")

        # Then
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=post.id).exists())

    def test_given_nonexistent_post_when_patching_then_returns_404(self):
        # Given
        non_existent_id = 999
        data = {"title": "Doesn't Matter", "content": "Still Doesn't Matter"}

        # When
        response = self.client.patch(f"/careers/{non_existent_id}/", data)

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "No Post matches the given query.")

    def test_given_nonexistent_post_when_deleting_then_returns_404(self):
        # Given
        non_existent_id = 999

        # When
        response = self.client.delete(f"/careers/{non_existent_id}/")

        # Then
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "No Post matches the given query.")
