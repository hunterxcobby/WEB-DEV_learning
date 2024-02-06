from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

def blog_page(request):
    return render(request, "blog/index.html")