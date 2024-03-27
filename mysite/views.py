from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from students.models import  *
from courses.models import  *
from .form import *

def my_site(request):
    courses = Course.objects.all()
    context = {
        "courses":courses
    }
    return render(request, 'my_site_index.html', context)




def user_register(request):
    form = User_Register_Form()
    if request.method == 'POST':
        form = User_Register_Form(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('my_site')
        else:
            pass
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_user(request):

    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('my_site')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('my_site')
