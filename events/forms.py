from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    # Remove the 'price' field from the form, so it's not rendered as a form field
    exclude = ['price']
