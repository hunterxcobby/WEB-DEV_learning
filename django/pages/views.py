from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# the hompage
def home(request):
    return(HttpResponse("<h1> Home Page</h1>"))

# about us 
def about(request):
    return(HttpResponse("<h1> About Us</h1>"))

# contact us 
def contact(request):
    return(HttpResponse("<h1> Contact Us</h1>"))

# services
def services(request):
    return(HttpResponse("<h1>Our Services</h1>"))