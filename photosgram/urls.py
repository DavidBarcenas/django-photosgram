"""photosgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from posts.views import list_posts
from users.views import login_view, logout_view, signup_view, update_profile


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('posts/', list_posts, name="feed"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name="signup"),
    path('users/me/profile', update_profile, name="update_profile"),
    # path('hello-world/', hello_world),
    # path('sorted/', obj_request),
    # path('hi/<str:name>/<int:age>/', say_hi),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
