from django import forms

from blogs.models import Post, BlogAuthor


class PostBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date', 'published_date')

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = BlogAuthor
#         fields = ('author_name')
