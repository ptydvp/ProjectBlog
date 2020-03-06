from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    create_time = models.TimeField()
    update_time = models.TimeField()
    status = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Comment(models.Model):
    content = models.TextField(null=True, blank=True)
    create_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=PROTECT)