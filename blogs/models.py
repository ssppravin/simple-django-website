from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True,)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class BlogAuthor(models.Model):
    author_name = models.CharField(max_length=100, blank=True)

class Contacts(models.Model):
    user_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=300)
    submitted_date = models.DateTimeField(default= timezone.now())

    class Meta:
        ordering = ('submitted_date',)

    def __str__(self):
        return self.user_name

    pass