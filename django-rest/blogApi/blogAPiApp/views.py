from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({"The setup was successful!"})

@api_view(['GET'])
def get_posts(request):
    pass