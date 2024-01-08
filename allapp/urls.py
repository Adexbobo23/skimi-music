from django.urls import path
from .views import ( home, genre, music, analytic, 
album, station, favorite, artist, history, profile, settings, plan
 )

urlpatterns = [
    path('home/', home, name='home'),
    path('genre/', genre, name='genre'),
    path('music/', music, name='music'),
    path('analytic/', analytic, name='analytic'),
    path('album/', album, name='album'),
    path('station/', station, name='station'),
    path('favorite/', favorite, name='favorite'),
    path('artist/', artist, name='artist'),
    path('history/', history, name='history'),
    path('plan/', plan, name='plan'),
    path('settings/', settings, name='settings'),
    path('profile/', profile, name='profile'),
]
