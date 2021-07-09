from django.forms.models import ModelForm
from posts.models import Post


class PostForm(ModelForm):
    """Post Model Form"""

    class Meta:
        """Form settings"""
        model = Post

        fields = ('user', 'profile', 'title', 'photo')