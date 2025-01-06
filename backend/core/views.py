from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


class  BlogCreate(generics.CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer

class  VolunteerCreate(generics.CreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

class  IssueCreate(generics.CreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class EventCreate(generics.CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class  BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class  IssueList(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer



class  EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class  CandidateList(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    
class  VolunteerList(generics.ListAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


class  WardList(generics.ListAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

    

class  CountyList(generics.ListAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer

    
class EventDetail(APIView):

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):  
        """
        Get a Event instance.
        """
        event= self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update an Event instance.
        """
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete an Event instance.
        """
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Get a Blog instance.
        """
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update a Blog instance.
        """
        blog  = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a Blog instance.
        """
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CandidateDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Get a Candidate instance.
        """
        event= self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

class IssueDetail(APIView):

    def get_object(self, pk):
        try:
            return Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Get a Issue instance.
        """
        issue = self.get_object(pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)
