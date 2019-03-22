from django import forms
from .models import Profile

classProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        