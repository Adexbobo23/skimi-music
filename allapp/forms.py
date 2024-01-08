from django import forms
from .models import MyProfile

class MyProfileForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = [ 'profile_image', 'first_name', 'last_name', 'display_name', 'location', 'about']