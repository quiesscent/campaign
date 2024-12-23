from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.


class  BlogCreate(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class  BlogList(APIView):
    def get(self, request):
        products = Blog.objects.all()
        serializer = BlogSerializer(products, many=True)
        return Response(serializer.data)


class EventCreate(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class  EventList(APIView):
    def get(self, request):
        products = Event.objects.all()
        serializer = EventSerializer(products, many=True)
        return Response(serializer.data)

