from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.views import View
from rest_framework.decorators import api_view

from blogs.forms import PostBlog
from blogs.models import Post, Contacts
from blogs.serializers import PostSerializer
from rest_framework.response import Response


def allPosts(request):
    all = Post.objects.all();
    # select * from post
    return render(request, 'blogs/blog.html', {'bloglist': all})


def detail(request, blogId):
    post = Post.objects.get(pk=blogId)
    context = {'post': post}
    return render(request, 'blogs/blogdetail.html', context)

@api_view(['GET'])
def api_post(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(Q(title__contains=query) | Q(text__contains=query))
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

def addPost(request):
    form = PostBlog()
    return render(request, 'blogs/addblog.html', {'form' : form})

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
            postss = form.save(commit=False)
            postss.save()
            # <process form cleaned data>
            return HttpResponseRedirect('/blog/')
        return render(request, self.template_name, {'form': form})


# def author(request):
#     form = AuthorForm()
#     return render(request, 'blogs/author.html', {'authorForm': form})

def contactForm(request):
    if request.method == "GET":
        return render(request, 'blogs/contactpage.html')
    elif request.method== "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            message = request.POST['message']
            contact = Contacts(user_name=name, email=email, mobile_number=mobile, message=message)
            contact.save()
            print("name = " + name)
            return render(request, 'blogs/contactpage.html', {'success' : True})
        except Exception as e:
            print("error in request")
            return  render(request, 'blogs/contactpage.html', {'success': False})