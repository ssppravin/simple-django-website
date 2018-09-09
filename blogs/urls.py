from blogs.views import AddPost
from . import views
from django.urls import path

urlpatterns = [
    path('', views.allPosts, name='blogs'),
    path('<int:blogId>/', views.detail, name='details'),
    path('add/', AddPost.as_view(), name='addpost'),
    path('api/', views.api_post, name='apipost')
    # path('author/', views.author, name='author')
    ]