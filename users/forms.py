from django import forms

class Profileform(forms.Form):
    website = forms.URLField(max_length=200, required=True,)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False,error_messages={'max_length': 'Please enter your name'})
    picture  = forms.ImageField()