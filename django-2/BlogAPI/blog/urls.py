
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page, name="blog_page"),
    path('blog-posts/', views.BlogPostList.as_view(), name='blogpost-list'),
    path('blog-posts/<int:pk>/', views.BlogPostDetail.as_view(), name='blogpost-detail')
]
