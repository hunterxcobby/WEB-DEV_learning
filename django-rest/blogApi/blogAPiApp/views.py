from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import postSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({"The setup was successful!"})


@api_view(['GET'])
def get_posts(request):
    get_all_posts = Post.objects.all()
    serializer = postSerializer(get_all_posts, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_post(request):
    serializer = postSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response({"success": "Post created successfully!"}, status=201)
