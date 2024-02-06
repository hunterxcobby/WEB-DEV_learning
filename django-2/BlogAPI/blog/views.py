from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def blog_page(request):
    return render(request, "blog/index.html")