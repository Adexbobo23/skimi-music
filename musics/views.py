from django.shortcuts import render, redirect
from .forms import MusicForm
from .models import Music
from allapp.models import MyProfile
from django.shortcuts import render, get_object_or_404


def add_music(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicForm()

    return render(request, 'add-music.html', {'form': form, 'my_profile': my_profile})


# def song_details(request, song_id):
#     song = get_object_or_404(Music, id=song_id)
#     return render(request, 'song_details.html', {'song': song})

def song_details(request, song_id):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None
    # Retrieve the song based on its ID or return a 404 error if not found
    song = get_object_or_404(Music, pk=song_id)

    context = {
        'song': song,
        'my_profile': my_profile
    }
    return render(request, 'song-details.html', context)