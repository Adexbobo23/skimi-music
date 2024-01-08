from django.urls import path
from .views import events, events_detail, create_event

urlpatterns = [
    path('allevents/', events, name='events'),
    # path('details/<int:event_id>/', events_detail, name='event_details'),
    path('details/', events_detail, name="event_details"),
    path('add/',create_event, name="addevent"),
]