from django.shortcuts import render

# Create your views here.
from blogs.models import Post


def allPosts(request):
    all = Post.objects.all();
    return render(request, 'blogs/blog.html', {'bloglist': all})