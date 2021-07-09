from django.urls import path
from posts.views import list_posts, create_post


urlpatterns = [
    path('', list_posts, name="feed"),
    path('posts/new/', create_post, name="create_post"),
]