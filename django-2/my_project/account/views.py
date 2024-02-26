from django.shortcuts import render,
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        user_name = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirm-password']
        email = request.POST['email']
        
        user = User.objects.create_user(username=username)

    else:
        return render(request, 'register.html')
