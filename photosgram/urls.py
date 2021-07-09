"""photosgram URL Configuration"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from posts.views import list_posts, create_post
from users.views import login_view, logout_view, signup_view, update_profile


urlpatterns = [
    path('', list_posts, name="feed"),
    path('posts/new/', create_post, name="create_post"),
    path('admin/', admin.site.urls, name="admin"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name="signup"),
    path('users/me/profile', update_profile, name="update_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
