from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # Importing Django's built-in registration form
from users.forms import CustomUserCreationForm  # Importing custom registration form
from django.contrib.auth import login, authenticate
from users.models import Profile
from meetings.models import Meeting
from django.contrib import messages

def welcome(request):
    return render(request, "website/welcome.html")

def about(request):
    return render(request, 'website/about.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use custom form
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)  # Create profile after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in as {}'.format(user.username))
            return redirect('welcome')  # Redirect to welcome page or other page after login
        else:
            messages.error(request, 'Registration failed. Please correct the errors in the form and try again.')
    else:
        form = CustomUserCreationForm()  # Use custom form
    return render(request, 'registration/register.html', {'form': form})

def login_success(request):
    messages.success(request, 'You are logged in as {}'.format(request.user.username))
    return redirect('welcome')

def logout_success(request):
    messages.success(request, 'You have successfully logged out. Log in to Add New Meeting.')
    return redirect('welcome')
