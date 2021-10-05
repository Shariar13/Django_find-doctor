from django.db import models
from django.db.models.fields.files import ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings 



# post
class post(models.Model):
    status=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author_name=models.CharField(max_length=19)
    author_email=models.CharField(max_length=100,null=True)
    post_author=models.CharField(max_length=100,null=True)
    

    def __str__(self):
        if len(self.status)>50:
            return self.status[:50]+"..."
        return self.status

    def get_absolute_url(self):
        return reverse("edit", kwargs={"pk": self.pk})
    


# comment
class comment(models.Model):
    comment=models.TextField()
    commenter_name=models.CharField(max_length=19)
    commenter_username=models.CharField(max_length=19,null=True)
    comment_date=models.DateTimeField(auto_now_add=True)
    comment_id=models.IntegerField(default=-1)
    post_author_name=models.CharField(max_length=99,null=True)
    def __str__(self):
        if len(self.comment)>50:
            return self.comment[:50]+"..."
        return self.comment

# this is a demo database of comment
class ans(models.Model):
    ans=models.TextField()
    ans_name=models.CharField(max_length=19)
    ans_date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(post,related_name="posts",on_delete=models.CASCADE)

    def __str__(self):
        if len(self.ans)>50:
            return self.ans[:50]+"..."
        return self.ans





# class profile_pic_model(models.Model):
#     user=models.CharField(max_length=100)
#     pic=models.ImageField(null=True,blank=True,upload_to='profilepicture/')

class profile_picture (models.Model):
    profile_picture_user= models.CharField(max_length=100)
    user_profile_picture=ImageField(upload_to='profilepicture/')



class feeds(models.Model):
    feed=models.TextField()
    name=models.CharField(max_length=99,default="Shariar Kabir")
    date=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=19,null=True)


    

    def __str__(self):
        if len(self.feed)>50:
            return self.feed[:50]+"..."
        return self.feed

    def get_absolute_url(self):
        return reverse("edit", kwargs={"pk": self.pk})


class social_media_account(models.Model):
    username=models.CharField(max_length=19)
    facebook=models.CharField(max_length=29,null=True)
    instagram=models.CharField(max_length=29,null=True)
    twitter=models.CharField(max_length=29,null=True)
    gmail=models.CharField(max_length=29,null=True)
    github=models.CharField(max_length=29,null=True)

class feedbacks(models.Model):
    feedbacker_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        if len(self.message)>50:
            return self.message[:50]+"..."
        return self.message

class contact_form_model(models.Model):
    name=models.CharField(max_length=99)
    email=models.CharField(max_length=99)
    message=models.TextField()

    def __str__(self):
        if len(self.message)>50:
            return self.message[:50]+"..."
        return self.message

class doctor (models.Model):
    username = models.CharField(max_length=99)
    name = models.CharField(max_length=99)
    email = models.CharField(max_length=99)
    phone = models.CharField(max_length=99)
    address = models.CharField(max_length=99)
    university = models.CharField(max_length=99)
    university_id = models.CharField(max_length=99)
    nid = models.CharField(max_length=99)
    status = models.CharField(max_length=99)
    category = models.CharField(max_length=99,default="Medicine Specialist")

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name