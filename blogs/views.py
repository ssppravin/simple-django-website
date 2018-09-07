from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from blogs.forms import PostBlog
from blogs.models import Post


def allPosts(request):
    all = Post.objects.all();
    # select * from post
    return render(request, 'blogs/blog.html', {'bloglist': all})


def detail(request, blogId):
    post = Post.objects.get(pk=blogId)
    context = {'post': post}
    return render(request, 'blogs/blogdetail.html', context)


# def addPost(request):
#     form = PostBlog()
#     return render(request, 'blogs/addblog.html', {'form' : form})

# def addPost(request):
#     if request.method == "POST":
#         form = PostBlog(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')
#     else:
#         form = PostBlog(initial={'title': 'value'})
#
#     return render(request, 'form_template.html', {'form': form})

class AddPost(View):
    form_class = PostBlog
    # initial = {'title', 'Latest News'}
    template_name = 'blogs/addblog.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/blog/')
        return render(request, self.template_name, {'form': form})

