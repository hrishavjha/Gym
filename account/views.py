from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import ExtendedUser


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    context = {
        'title': 'Register',
    }
    context = {
        'title': 'Login',
    }
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/services/')
        else:
            return render(request, "user/login.html", {"error": "Invalid Login Credentials."})
    else:
        return render(request, 'user/login.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    context = {
        'title': 'Register',
    }
    if request.method == "POST":
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'user/register.html', {'error': 'Username is already taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=password,
                                                email=request.POST['email'], first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'])
                ExtendedUser.ph_no = request.POST['phone']
                user.save()
                ExtendedUser.save()
            return redirect('/dashboard/')
        else:
            return render(request, 'user/register.html', {'error': 'Passwords dont match'})
    else:
        return render(request, 'user/register.html', context)
