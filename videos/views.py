from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoUploadForm
import random
from allapp.models import MyProfile


def upload_video(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploader = request.user
            video.save()
            return redirect('video')
    else:
        form = VideoUploadForm()
    return render(request, 'add-video.html', {'form': form, 'my_profile': my_profile})



def videos(request):
    try:
        my_profile = MyProfile.objects.get(user=request.user)
    except MyProfile.DoesNotExist:
        my_profile = None

    videos = list(Video.objects.all())
    random.shuffle(videos)
    return render(request, 'videos.html', {'videos': videos, 'my_profile': my_profile})

