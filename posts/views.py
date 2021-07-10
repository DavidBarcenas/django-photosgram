from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView
from django.shortcuts import redirect, render

from posts.forms import PostForm
from posts.models import Post


# Create your views here.
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 2
    context_object_name = 'posts'

@login_required
def create_post(request):
    """Create new post"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()


    return render(
        request, 
        'posts/new.html', 
        {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )