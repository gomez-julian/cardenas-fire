from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            domain = Subdomain.objects.all().filter(user = user).first()
            if domain:
                if domain.subdomain == 'CFS':
                    return redirect('cfs_dashboard')
            return redirect('index')
        else:
            return render(request, 'sign-in.html')
    return render(request, 'sign-in.html')

def signup_view(request):
    if request.method == 'POST':
        domains = ['CFS',]
        username = request.POST['username']
        password = request.POST['password']
        fullname = request.POST['fullname']
        subdomain = request.POST['subdomain']
        if subdomain in domains:
            user = User.objects.create_user(username = username, first_name = fullname, password = password)
            Subdomain.objects.create(subdomain = subdomain, user = user)
            return redirect('login_view')
        else:
            return render(request, 'sign-up.html')
    return render(request, 'sign-up.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')