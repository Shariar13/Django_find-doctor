from urllib.parse import quote
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from post.models import contact_form_model, post, profile_picture
from post.models import comment
from django.views import generic
from django.urls import reverse_lazy
from .forms import edit_post, social_form
from post.models import feeds
from post.models import social_media_account
from post.models import feedbacks
from django.contrib.auth.models import User
from post.models import doctor
from django.contrib import messages




class home(ListView):
    template_name = "index.html"
    model = post
    ordering = ['-id']
    

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('statuscategory')
    def get_context_data(self, *args, **kwargs):
        context = super(home, self).get_context_data(*args, **kwargs)
        context['social_media_account_list'] = social_media_account.objects.all()
        context['profile_picture_list'] = profile_picture.objects.all()
        context['feed_list'] = feeds.objects.all()
        context['doctor_list'] = doctor.objects.all()
        return context
    


def buy_me_a_coffee(request):
    return render (request,'payment.html')

def setting(request):
    return render(request, 'setting.html')



def signup(request):
    return render(request, 'signup.html')


class comments(generic.DetailView):
    model = post
    template_name = 'comment.html'
    ordering = ['-id']

  

    def get_context_data(self, *args, **kwargs):
        context = super(comments, self).get_context_data(*args, **kwargs)
        context['comment_list'] = comment.objects.all()
        context['doctor_list'] = doctor.objects.all()
        return context


class comments_for_feed(generic.DetailView):
    model = feeds
    template_name = 'comment_for_feed.html'
    ordering = ['-id']

  

    def get_context_data(self, *args, **kwargs):
        context = super(comments_for_feed, self).get_context_data(*args, **kwargs)
        context['comment_list'] = comment.objects.all()
        context['doctor_list'] = doctor.objects.all()
        return context


class edit(UpdateView):
    model=post
    form_class=edit_post
    template_name = 'edit.html'
    



class delete(DeleteView):
    model = post
    template_name = 'delete.html'
    fields = ['status']
    success_url = reverse_lazy('profile')

class delete_comment(DeleteView):
    model = comment
    template_name = 'delete_comment.html'
    fields = ['comment']
    # success_url=reverse_lazy("comments/53")
    def get_context_data(self, *args, **kwargs):
        context = super(delete_comment, self).get_context_data(*args, **kwargs)
        context['post'] = post.objects.all()
        return context
    success_url=("http://127.0.0.1:8000/comments/{comment_id}")






class user_profile(UpdateView):
    model=post
    form_class=edit_post
    template_name = 'edit.html'




class feed(ListView):
    template_name= "feed.html"
    model = feeds
    ordering = ['-id']
    

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('statuscategory')
    def get_context_data(self, *args, **kwargs):
        context = super(feed, self).get_context_data(*args, **kwargs)
        context['doctor_list'] = doctor.objects.all()
        return context

def feed_form (request):
    if request.method == "POST":
        feed = request.POST['feed']
        name = request.POST['name']
        category = request.POST['category']

        if feed == '':
            messages.error(request, 'You must be write something ! ')
            return redirect ('feed')
        else:
            feed_database=feeds(feed=feed,name=name,category=category)
            feed_database.save()
            return redirect ('feed')




class notification(ListView):
    template_name= "notification.html"
    model = comment
    ordering = ['-id']
    

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('statuscategory')


def social_media_form(request):
    if request.method=="POST":
        username=request.POST['username']
        facebook=request.POST['facebook']
        instagram=request.POST['instagram']
        twitter=request.POST['twitter']
        gmail=request.POST['gmail']
        github=request.POST['github']
        if social_media_account.objects.filter(username=username).exists():
            return HttpResponse ("you have already added your info")
        else:
            social_media_database=social_media_account(username=username,facebook=facebook,twitter=twitter,instagram=instagram,gmail=gmail,github=github)
            social_media_database.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class post_profile(generic.DetailView):
    model = post
    template_name = 'post_profile.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(post_profile, self).get_context_data(*args, **kwargs)
        context['profile_picture_list'] = profile_picture.objects.all()
        context['social_media_account_list'] = social_media_account.objects.all()
        return context



class doctor_profile(generic.DetailView):
    model = doctor
    template_name = 'doctor_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(doctor_profile, self).get_context_data(*args, **kwargs)
        context['profile_picture_list'] = profile_picture.objects.all()
        context['social_media_account_list'] = social_media_account.objects.all()
        return context










def report(request):
    return render(request,"report.html")

class share(DeleteView):
    model = post
    template_name = 'share.html'
    fields = ['status']
    success_url = reverse_lazy('profile')

def feedback(request):
    return render (request,"Feedback.html")

def feedback_form(request):
    if request.method=="POST":
        feedbacker_name=request.POST['username']
        email=request.POST['email']
        message=request.POST['feedback']
        feedback_database=feedbacks(feedbacker_name=feedbacker_name,email=email,message=message)
        feedback_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def contact(request):
    return render (request,"contact.html")

def contact_form(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        contact_database=contact_form_model(name=name,email=email,message=message)
        contact_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def about(request):
    return render (request, "about.html")

def search (request):
    if request.method == 'POST':
        search = request.POST['search']
        Doctor_list = doctor.objects.filter(name__contains = search)
        Feed_list = feeds.objects.filter(feed__contains = search)
        Post_list = post.objects.filter(status__contains = search)
        User_list = User.objects.filter(first_name__contains = search)
        return render (request, 'search.html',{'search':search,'Doctor_list':Doctor_list,'Feed_list':Feed_list,'Post_list':Post_list,'User_list':User_list})
    else:
        return render (request, "search.html")

def shop (request):
    return render (request, "shop.html")

class doctor_category (ListView):
    template_name = "find_doctor.html"
    model = doctor
    ordering = ['-id']

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related
        ('statuscategory')



    


    

   



