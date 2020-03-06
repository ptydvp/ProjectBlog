from django.contrib import admin
from management.models import Post, User, Comment

# Register your models here.

admin.site.register(User)

admin.site.register(Post)

admin.site.register(Comment)