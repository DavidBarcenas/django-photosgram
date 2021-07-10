from users.models import Profile
from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    styles = attrs={'class': 'form-control'}
    _max_length = 50

    username   = forms.CharField(min_length=4, max_length=_max_length, widget=forms.TextInput(styles))
    first_name = forms.CharField(min_length=2, max_length=_max_length, widget=forms.TextInput(styles))
    last_name  = forms.CharField(min_length=2, max_length=_max_length, widget=forms.TextInput(styles))
    email      = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput(styles))
    password   = forms.CharField(widget=forms.PasswordInput(styles))
    password_confirm = forms.CharField(widget=forms.PasswordInput(styles))

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use.')

        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirm = data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirm')

        user = User.objects.create_user(**data)

        profile = Profile(user=user)
        profile.save()
