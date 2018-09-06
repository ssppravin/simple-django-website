
from . import views
from django.urls import path

urlpatterns = [
    path('', views.intro, name='department'),
    path('about', views.index, name='index'),
    path('course', views.courses, name='course'),
    path('course/python', views.pythondepart, name='python'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('team', views.teams, name='teams'),
]
