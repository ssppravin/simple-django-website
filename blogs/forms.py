from django import forms

from blogs.models import Post


class PostBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date')
