from django.urls import path
from .views import PostList, PostDetail , delete_post

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('api/posts/<int:pk>/delete/', delete_post, name='delete-post'),
]
