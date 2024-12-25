from rest_framework import serializers
from .models import Blog, Event

class BlogSerializer(serializers.ModelSerializer):
    rendered_content = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog 
        fields = ['id', 'title', 'description', 'content', 'image', 'rendered_content']

    def get_rendered_content(self, obj):
        return obj.formatted_content()

class EventSerializer(serializers.ModelSerializer):
    rendered_content = serializers.SerializerMethodField()
    
    class Meta:
        model = Event 
        fields = ['title', 'content', 'date', 'venue', 'location', 'image', 'rendered_content' ]
    
    def get_rendered_content(self, obj):
        return obj.formatted_content()
