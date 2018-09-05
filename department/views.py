from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from department.models import Courses, Testimonial


def department(request):
    return HttpResponse("test");

def index(request):
    return render(request, 'department/mydepartment.html')

def courses(request):
    allCourses = Courses.objects.all()
    return render(request, 'department/courses.html', {'data' : allCourses})

def intro(request):
    return render(request, 'department/intro.html', {'name':'Broadyway Department', 'address':'Kathmandu'})

def pythondepart(request):
    return render(request, 'department/pythondepartment.html')

def testimonial(request):
    data = Testimonial.objects.all();
    return render(request, 'department/testimonial.html', {'testimonials' : data})

def teams(request):
    allTestimonial = Testimonial.objects.all()
    return render(request, 'department/team.html', {'data':allTestimonial[0]})