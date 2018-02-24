from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def index(request):
    return HttpResponse("Test1 blog")

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        srl = PostSerializer(posts, many=True)
        return Response(srl.data)


