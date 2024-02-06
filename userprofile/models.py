from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
    about = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    RELATIONSHIP_CHOICES = [
        ('Single', 'Single'),
        ('In a relationship', 'In a relationship'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Complicated', 'Complicated'),
    ]
    relationship_status = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES, blank=True)
    location = models.CharField(max_length=255, blank=True)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True)
    email_address = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Additional Fields
    hobbies = models.TextField(blank=True)
    favourite_movies = models.TextField(blank=True)
    favourite_books = models.TextField(blank=True)
    favourite_games = models.TextField(blank=True)
    favourite_bands_artists = models.TextField(blank=True)
    favourite_series = models.TextField(blank=True)
    other_interest = models.TextField(blank=True)
    education = models.TextField(blank=True)
    work = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
