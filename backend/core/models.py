from django.db import models
from django.utils.timezone import now
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from datetime import time, date
from django.core.validators import MinValueValidator, MaxValueValidator
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

class Policies(models.Model):
    title = models.CharField(max_length=10000000000, default='')
    image = models.ImageField(upload_to='policies/', default='')
    file =  models.FileField(upload_to='uploads/documents/')


class Tag(models.Model):
    name = models.CharField(max_length=10000, default='')
    policies = models.ForeignKey(Policies, on_delete=models.CASCADE, related_name='tags', default=1)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=1000, default='')

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length=20, default='')

    class Meta:
        verbose_name_plural = 'Counties'

    def __str__(self):
        return f'{self.name}'

class Constituency(models.Model):
    name = models.CharField(max_length=20, default='')
    county = models.ForeignKey(County, related_name='constituency', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Constituencies'
   
    def __str__(self):
        return f'{self.name}'

class Ward(models.Model):
    name = models.CharField(max_length=20, default='')
    constituency = models.ForeignKey(Constituency, related_name='ward', on_delete=models.CASCADE, default=1)

   
    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    title = models.CharField(max_length=10000, default='')
    content = MarkdownxField()
    description = models.TextField(default='')
    date = models.DateField(default=date.today)
    time = models.TimeField(default=time(8, 0))
    venue = models.CharField(default='', max_length=100000000000)
    attendees = models.IntegerField(default=1)
    location = models.CharField(default='', max_length=100000000)
    image = models.ImageField(upload_to='events/', default='events.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    def formatted_content(self):
        # Convert Markdown content to HTML
        return markdownify(self.content)
    
    def __str__(self):
        return self.title

class Volunteer(models.Model):
    email = models.CharField(default='', max_length=1000)
    zipcode = models.CharField(default='', max_length=100)
    phone = models.IntegerField(validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(99999999999999)  
        ])
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
    content = models.TextField(default='')
    level =  models.CharField(max_length=20, choices=ISSUE_LEVEL) 
    county =  models.ForeignKey(County, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)


    def __str__(self):
        return f'A {self.level} issue level on {self.title}'

class Transaction(models.Model):
    receipt = models.CharField(max_length=255, null=True, blank=True)  # New IntegerField
    reference = models.CharField(max_length=255, null=True, blank=True)  # Optional
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    checkout_request_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.receipt} payment for {self.reference}"


class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(99999999999999)  
        ])
    county =  models.ForeignKey(County, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    skills = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Members"

    def __str__(self):
        return f"{self.first_name} {self.last_name} from {self.county}"

class Order(models.Model):
    ORDER_STATUS = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    )
    name = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    address = models.CharField(max_length=100, default='')
    item = models.CharField(max_length=100, default='')
    quantity = models.CharField(max_length=100, default='')
    sizes = models.CharField(max_length=100, default='', null=True, blank=True)
    color = models.CharField(max_length=100, default='', null=True, blank=True)
    status =  models.CharField(max_length=20, choices=ORDER_STATUS)
    def __str__(self):

        return f'Order by {self.name} status {self.status}'
