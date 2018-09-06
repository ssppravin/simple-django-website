from django.db import models

# Create your models here.
from django.db import models

class Courses(models.Model):
    course_name = models.CharField(max_length=300)
    fees = models.CharField(max_length=100, default="0")
    trainer_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name + "" + self.fees + "\t\t" + self.trainer_name

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True)
    skill = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    image = models.FileField(upload_to="testimonial", blank=True)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()