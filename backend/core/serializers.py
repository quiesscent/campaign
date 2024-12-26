from rest_framework import serializers
from .models import Blog, Event, Volunteer, Ward, Issue, County, Policies , Candidate

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

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate 
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields = '__all__'


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    rendered_content = serializers.SerializerMethodField()
    class Meta:
        model = Issue
        fields = ['title', 'content', 'level', 'county', 'ward', 'rendered_content']

    def get_rendered_content(self, obj):
        return obj.formatted_content()
