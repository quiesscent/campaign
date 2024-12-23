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
    serializer_class = BlogSerializer


class EventCreate(generics.CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class  BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        # Get the standard response
        response = super().list(request, *args, **kwargs)

        # Return only the 'results' part with a 200 OK status
        return Response(response.data['results'], status=status.HTTP_200_OK)


class  EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    
    def list(self, request, *args, **kwargs):
        # Get the standard response
        response = super().list(request, *args, **kwargs)

        # Return only the 'results' part with a 200 OK status
        return Response(response.data['results'], status=status.HTTP_200_OK)


class EventDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event= self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        blog  = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
