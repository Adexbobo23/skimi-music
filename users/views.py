from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserLoginForm
from userprofile.models import UserProfile 


@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the user's profile page without specifying 'username'
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    
    return render(request, 'login.html')


from django.contrib.auth import logout  
from django.shortcuts import redirect

def custom_logout(request):
    logout(request) 
    return redirect('login')
