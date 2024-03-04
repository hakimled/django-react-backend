from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, parsers
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-id', '-likes')
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser]

    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return JsonResponse({'message': 'Post deleted successfully'})
