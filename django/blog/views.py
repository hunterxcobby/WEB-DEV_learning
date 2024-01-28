from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request, article_id=''):
        return HttpResponse(f"<h1> Blog {article_id}</h1>")
