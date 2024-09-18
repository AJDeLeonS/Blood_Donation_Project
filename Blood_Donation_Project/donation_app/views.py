from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from .models import CustomUser, Profile
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        user_form = CustomUser(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile creation
    else:
        user_form = CustomUser()
    return render(request, 'register.html', {'form': user_form})

def profile(request):
    if request.method == 'POST':
        profile_form = Profile(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')  # After profile completion
    else:
        profile_form = Profile(instance=request.user.profile)
    return render(request, 'profile.html', {'form': profile_form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if Profile.objects.filter(user=user).exists():
                return redirect('home')  # If profile exists, go to home
            else:
                return redirect('complete_profile')
    return render(request, 'login.html')

def load_provinces(request):
    region = request.GET.get('region')
    # Logic to return the provinces based on the region
    return JsonResponse(list(provinces), safe=False)

def load_municipalities(request):
    province = request.GET.get('province')
    # Logic to return the municipalities based on the province
    return JsonResponse(list(municipalities), safe=False)

def home(request):
    return render(request, 'home.html')


