from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        user_name = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirm-password']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Username is already taken...")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "Account created successfully")
        else:
            messages.info(request, "Password does not match ")
            
        return redirect('/')
    else:
        return render(request, 'register.html')
