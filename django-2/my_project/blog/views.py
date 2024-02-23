from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return render(request, 'blog.html', {'name': 'Cobby'} )

def add(request):
    return render(request, 'result.html')