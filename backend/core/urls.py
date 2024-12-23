from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/create', BlogCreate.as_view(), name='create_blog'),
    path('events/create', EventCreate.as_view(), name='create_event'),
    path('blogs', BlogList.as_view(), name='blogs'),
    path('events', EventList.as_view(), name='events'),
    path('events/<int:pk>', EventDetail.as_view(), name='e_detail'),
    path('blogs/<int:pk>', BlogDetail.as_view(), name='b_detail'),
]
