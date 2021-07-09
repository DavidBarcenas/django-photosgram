from django.urls import path
from django.views.generic import TemplateView
from users.views import login_view, logout_view, signup_view, update_profile


urlpatterns = [
    path('<str:username>/', TemplateView.as_view(template_name="users/detail"), name='detail'),
    path('users/login/', login_view, name="login"),
    path('users/logout/', logout_view, name="logout"),
    path('users/signup/', signup_view, name="signup"),
    path('users/me/profile/', update_profile, name="update_profile"),
]