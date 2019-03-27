from django import forms
from .models import Profile,Image,Comments,Like

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile']

class CommentsForm(forms.Form):

     comment =forms.CharField(label='Comment',max_length = 300)
    

class LikesForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['user','image']

        