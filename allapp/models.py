from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class MyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()

    # You can add an image field to store the user's profile picture
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.user.username
