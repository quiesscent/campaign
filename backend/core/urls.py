from django.urls import path
from .views import *
from .mpesa import *
from .order import *

urlpatterns = [
    path('issues/create', IssueCreate.as_view(), name='create_issue'),
    path('volunteers/create', VolunteerCreate.as_view(), name='volunteer'),
    path('orders/create', OrdersCreate.as_view(), name='orders'),
    path('join', JoinView.as_view(), name='join'),
    path('members', MemberList.as_view(), name='members'),
    path('blogs', BlogList.as_view(), name='blogs'),
    path('policies', PolicyList.as_view(), name='policy'),
    path('issues', IssueList.as_view(), name='issues'),
    path('events', EventList.as_view(), name='events'),
    path('candidates', CandidateList.as_view(), name='candidates'),
    path('feedback', FeebackView.as_view(), name='feedback'),
    # path('counties', CountyList.as_view(), name='counties'),
    # path('constituencies/<int:county>', ConstituencyList.as_view(), name='constituencies'), 
    # path('wards/<int:constituency>', WardList.as_view(), name='wards'),
    path('events/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('issues/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('blogs/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
    path('candidates/<int:pk>', CandidateDetail.as_view(), name='candidate_detail'),
    path('campaign_stkpush', StkPushView.as_view(), name='stkpush'),
    path('order_stkpush', OrderStkPushView.as_view(), name='order_stkpush'),
    path('campaign_callback', mpesa_callback , name='callbak'),
    path('order_callback', order_mpesa_callback , name='order_callbak'),
]
