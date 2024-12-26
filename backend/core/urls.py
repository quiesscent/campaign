from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/create', BlogCreate.as_view(), name='create_blog'),
    path('events/create', EventCreate.as_view(), name='create_event'),
    path('volunteers/create', VolunteerCreate.as_view(), name='volunteer'),
    path('blogs', BlogList.as_view(), name='blogs'),
    path('events', EventList.as_view(), name='events'),
    path('candidates', CandidateList.as_view(), name='candidates'),
    path('counties', CountyList.as_view(), name='counties'),
    path('wards', WardList.as_view(), name='wards'),
    path('volunteers', VolunteerList.as_view(), name='volunteers'),
    path('events/<int:pk>', EventDetail.as_view(), name='e_detail'),
    path('blogs/<int:pk>', BlogDetail.as_view(), name='b_detail'),
    path('candidates/<int:pk>', CandidateDetail.as_view(), name='candiate_detail'),
]
