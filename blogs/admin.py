from django.contrib import admin

# Register your models here.
from blogs.models import Post, BlogAuthor

admin.site.register(Post)
admin.site.register(BlogAuthor)