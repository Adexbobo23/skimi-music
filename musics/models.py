from django.db import models
from django.conf import settings

class Music(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    composer = models.CharField(max_length=255)
    lyricist = models.CharField(max_length=255)
    music_director = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[
        ('Remix', 'Remix'),
        ('Pop', 'Pop'),
        ('DJ', 'DJ'),
        ('hippop', 'hippop'),
    ])
    lyrics = models.TextField()
    is_free = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    song_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cover_image = models.ImageField(upload_to='music_covers/')
    music_file = models.FileField(upload_to='music_files/')
    duration = models.CharField(max_length=10)  # Use CharField to store duration as a string

    def __str__(self):
        return self.song_name
