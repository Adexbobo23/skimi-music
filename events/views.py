from django.shortcuts import render
from .models import Event 
from django.shortcuts import render, get_object_or_404
from musics.models import Music
from allapp.models import MyProfile

def events(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None
    # Query all events
    all_events = Event.objects.all()
    music = Music.objects.all()[:10]
    
    # Render the template with the events as context
    return render(request, 'events.html', {'all_events': all_events, 'all_music': music, 'my_profile': my_profile})


# def events_detail(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     return render(request, 'event-details.html', {'event': event})

def events_detail(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None
    music = Music.objects.all()[:10]
    return render(request, 'event-details.html', {'all_music': music, 'my_profile': my_profile})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventForm 
import logging

logger = logging.getLogger(__name__)

def create_event(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None
        
    music = Music.objects.all()[:10]
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully')
            return redirect('events')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            logger.error(f"Form is invalid: {form.errors}")
    else:
        form = EventForm()
    
    return render(request, 'add-event.html', {'form': form, 'all_music': music, 'my_profile': my_profile})

