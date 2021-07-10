from django.urls import path
from posts.views import CreatePostView, PostDetailView, PostsFeedView


urlpatterns = [
    path('', PostsFeedView.as_view(), name="feed"),
    path('posts/new/', CreatePostView.as_view(), name="create_post"),
    path('<int:id>', PostDetailView.as_view(), name="detail"),
]