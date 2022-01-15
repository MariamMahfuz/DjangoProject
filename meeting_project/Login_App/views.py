from django.shortcuts import redirect, render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.

def register_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            if User.objects.filter(username=username).first():
                messages.success(request, "username is already taken")
                return redirect('/register')

            if User.objects.filter(email=email).first():
                messages.success(request, "email already taken")
                return redirect('/register')
            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            profile_obj=Profile.objects.create(User=user_obj)
            profile_obj.save()
        except Exception as e:
            print(e)

    dict = {}
    return render(request, 'Login_App/register.html', context=dict)


def Login_attempt(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.warning(request,"User Not Found")
            return redirect('/login/')
        Profile_obj=Profile.objects.filter(User=user_obj).first()
        if not Profile_obj.is_verified:
            messages.success(request,"Profile is not varified,check your mail")
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.success(request,"Wrong Password")
            return redirect('/login/')
        login(request,user)
        return redirect('/')



    dict = {}
    return render(request, 'Login_App/login.html', context=dict)
