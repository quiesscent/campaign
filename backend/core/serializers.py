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
        fields = ['id', 'title', 'file', 'image', 'tags']


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ['number']

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['number']

class ConstituencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
        fields = ['number']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'content', 'level', 'county', 'ward']


class JoinUsSerializer(serializers.ModelSerializer):
    county = serializers.IntegerField(write_only=True) 
    ward = serializers.IntegerField(write_only=True) 
    constituency = serializers.IntegerField(write_only=True)

    class Meta:
        model = Members
        fields = ['id', 'firstname', 'lastname', 'email', 'phone', 'skills', 'county', 'ward', 'constituency']

    def create(self, validated_data):
        county_number = validated_data.pop('county')
        ward_number = validated_data.pop('ward')
        constituency = validated_data.pop('constituency')

        # Fetch the county and ward instances using the number fields
        county = County.objects.get(number=county_number)
        ward = Ward.objects.get(number=ward_number) 
        constituency = Constituency.objects.get(number=constituency)

        member = Members.objects.create(county=county, ward=ward, **validated_data)
        # member.save()
        return member

class StkPushSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(
        min_value=254000000000,  # Example minimum value for Kenyan phone numbers
        max_value=2549999999999,  # Example maximum value for Kenyan phone numbers
        help_text="The phone number to send STK Push to, e.g., 7xxxxxxxx."
    )
    amount = serializers.IntegerField(
        min_value=1,  # Ensure the amount is at least 1
        help_text="The amount to transact.",
    )
   

class OrderStkPushSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(
        min_value=254000000000,  # Example minimum value for Kenyan phone numbers
        max_value=2549999999999,  # Example maximum value for Kenyan phone numbers
        help_text="The phone number to send STK Push to, e.g., 7xxxxxxxx."
    )
    amount = serializers.IntegerField(
        min_value=1,  # Ensure the amount is at least 1
        help_text="The amount to transact.",
    )
