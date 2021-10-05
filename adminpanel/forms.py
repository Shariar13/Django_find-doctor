from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView, TemplateView, UpdateView
from django.contrib.auth.models import User
from post.models import post
from post.models import social_media_account



class edit_post(forms.ModelForm):
    status=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    

    class Meta:
        model = post
        fields = ('status',)


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

    # def __init__(self, *args, **kwargs):
    #     super(UserChangeForm, self).__init__(*args, **kwargs)