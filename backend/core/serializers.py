from rest_framework import serializers
from .models import Blog, Event

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog 
        fields = ['id', 'title', 'description', 'content', 'image']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = '__all__'

