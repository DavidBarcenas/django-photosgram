from django.urls import path
from users.views import SignupView, UpdateProfileView, login_view, logout_view, UserDetailView


urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('me/profile/', UpdateProfileView.as_view(), name="update_profile"),
    path('<str:username>/', UserDetailView.as_view(), name='detail'),
]