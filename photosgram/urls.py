"""photosgram URL Configuration"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('admin/', admin.site.urls, name="admin"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 