from django.db import models


class PostManager(models.Manager):
    pass


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, null=False, blank=False)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField(max_length=512, null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)

    objects = PostManager()
