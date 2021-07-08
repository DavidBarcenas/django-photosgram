from django import forms

class Profileform(forms.Form):
    picture  = forms.ImageField()
    website = forms.URLField(max_length=200, required=True,)
    biography = forms.CharField(max_length=250, required=False)
    phone_number = forms.CharField(
        max_length=20, 
        required=False,
        error_messages={
            'max_length': 'The phone number field is for a maximum of 20 characters'
        }
    )