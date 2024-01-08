from django.urls import path
from .views import videos, upload_video


urlpatterns = [
    path('videos/', videos, name="video"),
    path('upload/', upload_video, name='addvideo'),
]