from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

from users.forms import SignupForm
from users.models import Profile
from posts.models import Post


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context ['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and/or password'})

    return render(request, 'users/login.html')


class SignupView(FormView):
    """Users signup view"""   

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update user profile"""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""

        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')