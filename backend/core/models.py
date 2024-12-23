from django.db import models
from django.utils.timezone import now
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1000000, default='')
    description = models.TextField(default='')
    content = models.TextField(default='')
    image = models.ImageField(upload_to='blogs/', default='blog.png')
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=10000, default='')
    content = models.TextField(default='')
    date = models.DateTimeField()
    venue = models.CharField(default='', max_length=100000000000)
    location = models.CharField(default='', max_length=100000000)
    image = models.ImageField(upload_to='events/', default='events.png')
    

    def __str__(self):
        return self.title
