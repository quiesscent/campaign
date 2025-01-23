from rest_framework import serializers
from .models import *



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BlogCreateSerializer(serializers.ModelSerializer):    
    rendered_content = serializers.SerializerMethodField()
    class Meta:
        model = Blog 
        fields = ['id', 'title', 'description', 'content', 'image', 'rendered_content']

    def get_rendered_content(self, obj):
        return obj.formatted_content()

class BlogSerializer(serializers.ModelSerializer):
    rendered_content = serializers.SerializerMethodField()
    class Meta:
        model = Blog 
        fields = ['id', 'title', 'description', 'content', 'image', 'rendered_content',  'created_at' ]

    def get_rendered_content(self, obj):
        return obj.formatted_content()

class EventSerializer(serializers.ModelSerializer):
    rendered_content = serializers.SerializerMethodField()
    
    class Meta:
        model = Event 
        fields = ['id', 'title', 'content', 'description', 'date', 'time', 'venue', 'location', 'image', 'rendered_content', 'category' ]
    
    def get_rendered_content(self, obj):
        return obj.formatted_content()

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate 
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Policies
        fields = ['file', 'image', 'tags']


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'

class ConstituencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
        fields = '__all__'
    
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'content', 'level', 'county', 'ward']

class JoinUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class StkPushSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(
        min_value=254000000000,  # Example minimum value for Kenyan phone numbers
        max_value=2549999999999,  # Example maximum value for Kenyan phone numbers
        help_text="The phone number to send STK Push to, e.g., 7xxxxxxxx."
    )
    amount = serializers.IntegerField(
        min_value=50,  # Ensure the amount is at least 1
        help_text="The amount to transact.",
    )
    account_reference = serializers.CharField(
        max_length=10000000,
        help_text="The account reference for the transaction."
    )
