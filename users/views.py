from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('course_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose a different one.")
            return redirect('register')  # Adjust the redirect URL as needed
        
        # Proceed with the rest of the registration process
        # Assuming other necessary fields are handled as well
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        messages.success(request, "Registration successful!")
        return redirect('login')  # Redirect to a login page or desired URL

    return render(request, 'users/register.html')
