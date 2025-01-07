from django.urls import path
from .views import *
from .mpesa import *
urlpatterns = [
    path('blogs/create', BlogCreate.as_view(), name='create_blog'),
    path('issues/create', IssueCreate.as_view(), name='create_issue'),
    path('events/create', EventCreate.as_view(), name='create_event'),
    path('volunteers/create', VolunteerCreate.as_view(), name='volunteer'),
    path('join', JoinView.as_view(), name='join'),
    path('members', MemberList.as_view(), name='members'),
    path('blogs', BlogList.as_view(), name='blogs'),
    path('issues', IssueList.as_view(), name='issues'),
    path('events', EventList.as_view(), name='events'),
    path('candidates', CandidateList.as_view(), name='candidates'),
    path('counties', CountyList.as_view(), name='counties'),
    path('wards/<int:county>', WardList.as_view(), name='wards'),
    path('volunteers', VolunteerList.as_view(), name='volunteers'),
    path('events/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('issues/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('blogs/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
    path('candidates/<int:pk>', CandidateDetail.as_view(), name='candidate_detail'),
    path('stkpush', StkPushView.as_view(), name='stkpush'),
]
