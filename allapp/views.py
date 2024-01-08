from userprofile.models import UserProfile
from musics.models import Music
from random import shuffle
from django.shortcuts import render, redirect
from .models import MyProfile
from .forms import MyProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MyProfile

@login_required(login_url='login')
def home(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    

    # Fetch only the first 10 music items
    all_music = Music.objects.all()[:10]

    # Fetch the first 10 most recently added music items
    recent_music = Music.objects.order_by('-id')[:10]

    # Fetch the first 10 song cover images and artist names
    song_data = Music.objects.all()[:10].values('cover_image', 'artist')

    return render(request, 'home.html', {'user_profile': user_profile, 'all_music': all_music, 'recent_music': recent_music, 'song_data': song_data, 'my_profile': my_profile})


@login_required(login_url='login')
def genre(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    all_music = Music.objects.all()[:10]
    return render(request, 'genres.html', {'all_music': all_music, 'my_profile': my_profile})


@login_required(login_url='login')
def music(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    # Fetch all music data from the database
    all_music = Music.objects.all()
    music = Music.objects.all()[:10]
    # Shuffle the music list
    music_list = list(all_music)
    shuffle(music_list)
    shuffled_music = music_list

    context = {
        'music_list': all_music,
        'all_music': music,
        'shuffled_music': shuffled_music,
        'my_profile': my_profile
    }

    return render(request, 'music.html', context)


@login_required(login_url='login')
def album(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    all_music = Music.objects.all()
    music = Music.objects.all()[:10]
    # Shuffle the music list
    music_list = list(all_music)
    shuffle(music_list)

    context = {
        'music_list': all_music,
        'all_music': music,
        'my_profile': my_profile
    }
    return render(request, 'albums.html', context)


@login_required(login_url='login')
def artist(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    all_music = Music.objects.all()
    music = Music.objects.all()[:10]

    context = {
        'music_list': all_music,
        'all_music': music,
        'my_profile': my_profile
    }

    return render(request, 'artists.html', context)


@login_required(login_url='login')
def station(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    music = Music.objects.all()[:10]
    return render(request, 'stations.html', {'all_music': music, 'my_profile': my_profile})


@login_required(login_url='login')
def analytic(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    music = Music.objects.all()[:10]
    return render(request, 'analytics.html', {'all_music': music, 'my_profile': my_profile})


@login_required(login_url='login')
def favorite(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    music = Music.objects.all()
    return render(request, 'favorites.html', {'all_music': music, 'my_profile': my_profile})


@login_required(login_url='login')
def history(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    music = Music.objects.all()[:10]
    return render(request, 'history.html', {'all_music': music, 'my_profile': my_profile})


@login_required(login_url='login')
def profile(request):
    try:
        my_profile, created = MyProfile.objects.get_or_create(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None

    if request.method == 'POST':
        form = MyProfileForm(request.POST, request.FILES, instance=my_profile)
        if form.is_valid():
            my_profile = form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Profile update failed. Please check the form data.')
    else:
        form = MyProfileForm(instance=my_profile)

    return render(request, 'profile.html', {'form': form})


@login_required(login_url='login')
def settings(request):
    music = Music.objects.all()[:10]
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None
    return render(request, 'settings.html', {'all_music': music, 'my_profile': my_profile})



@login_required(login_url='login')
def plan(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None    
    music = Music.objects.all()[:10]
    return render(request, 'plan.html', {'all_music': music, 'my_profile': my_profile})