from django.contrib import admin

# Register your models here.
from department.models import Courses, Musician, Album, Testimonial

admin.site.register(Courses)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Testimonial)