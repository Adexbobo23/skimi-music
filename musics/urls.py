from django.urls import path
from .views import add_music, song_details

urlpatterns = [
    path('add/', add_music, name='addmusic'),
    # path('song/<int:song_id>/', song_details, name='song_details'),
     path('song/<int:song_id>/', song_details, name='song_details'),
]