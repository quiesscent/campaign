from django.db import models
from django.utils.timezone import now
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=1000000, default='')
    description = models.TextField(default='')
    content = MarkdownxField()
    image = models.ImageField(upload_to='blogs/', default='blog.png')
    created_at = models.DateTimeField(default=now)


    def formatted_content(self):
        # Convert Markdown content to HTML
        return markdownify(self.content)

    def __str__(self):
        return self.title

class County(models.Model):
    name = models.CharField(max_length=20, default='')

    class Meta:
        verbose_name_plural = 'Counties'

    def __str__(self):
        return f'{self.name}'


class Ward(models.Model):
    name = models.CharField(max_length=20, default='')
    county = models.ForeignKey(County, related_name='ward', on_delete=models.CASCADE)

   
    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    title = models.CharField(max_length=10000, default='')
    content = MarkdownxField()
    date = models.DateTimeField()
    venue = models.CharField(default='', max_length=100000000000)
    location = models.CharField(default='', max_length=100000000)
    image = models.ImageField(upload_to='events/', default='events.png')
    
    def formatted_content(self):
        # Convert Markdown content to HTML
        return markdownify(self.content)
    
    def __str__(self):
        return self.title

class Policies(models.Model):
    title = models.CharField(max_length=10000000000, default='')
    file =  models.FileField(upload_to='uploads/documents/')


class Volunteer(models.Model):
    full_name = models.CharField(default='', max_length=20)
    role = models.CharField(default='', max_length=100)
    skills = models.TextField()
    phone_number = models.IntegerField()
    county =  models.ForeignKey(County, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.full_name}'


class Candidate(models.Model):
    name = models.CharField(max_length=1000000, default='')
    position = models.CharField(max_length=1000, default='')
    about = models.TextField(default='')
    county =  models.ForeignKey(County, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} for {self.position} in {self.county}'
    
class Issue(models.Model):
    ISSUE_LEVEL = (
        ('national', 'National'),
        ('county', 'County'),
        ('ward', 'Ward'),
    )
    title = models.TextField()
    content = MarkdownxField()
    level =  models.CharField(max_length=20, choices=ISSUE_LEVEL) 
    county =  models.ForeignKey(County, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)


    def __str__(self):
        return f'A {self.level} issue level on {self.title}'

