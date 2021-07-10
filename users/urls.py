from django.urls import path
from users.views import login_view, logout_view, signup_view, update_profile, UserDetailView


urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup_view, name="signup"),
    path('me/profile/', update_profile, name="update_profile"),
    path('<str:username>/', UserDetailView.as_view(), name='detail'),
]