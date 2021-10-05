from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import social_media_account



class edit_profile_form(UserChangeForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    #email=forms.CharField(widget=forms.EmailField(attrs={'class':'form-control'}))
    

    class Meta:
        model = User
        fields = ('first_name','last_name','username')


class social_form(forms.ModelForm):
    facebook=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    instagram=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    twitter=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    gmail=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    github=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    #email=forms.CharField(widget=forms.EmailField(attrs={'class':'form-control'}))
    

    class Meta:
        model = social_media_account
        fields = ('facebook','instagram','twitter','gmail','github',)


 