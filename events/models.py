from django.db import models
from django.conf import settings

class Event(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    COVER_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
    ]

    cover_image = models.ImageField(upload_to='event_covers/', null=True, blank=True)
    event_name = models.CharField(max_length=255)
    event_venue = models.TextField()
    event_date = models.DateField()
    organizer_email = models.EmailField()
    organizer_phone = models.CharField(max_length=20)
    event_seats = models.IntegerField()
    description = models.TextField()
    price = models.CharField(max_length=4, choices=COVER_CHOICES, default='free')
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.event_name
