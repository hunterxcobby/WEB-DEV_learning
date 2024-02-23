from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return render(request, 'blog.html', {'name': 'Cobby'} )

def add(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    result = val1 + val2

    return render(request, 'result.html', {'result': result})