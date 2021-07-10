from django.urls import path
from posts.views import PostsFeedView, create_post


urlpatterns = [
    path('', PostsFeedView.as_view(), name="feed"),
    path('posts/new/', create_post, name="create_post"),
]