from django.contrib import admin
from django.urls import path
from .import views
from  .views import edit_profile
from  .views import edit_social_media
from  .views import profile_pic_change




urlpatterns = [
   
    path('',views.profile.as_view(),name='profile'),
    path('status_form/',views.status_form,name='status_form'),
    path('comment_form/',views.comment_form,name='comment_form'),
    path('profile_pic/',views.profile_pic,name='profile_pic'),
    path('edit_profile/',edit_profile.as_view(),name='edit_profile'),
    path('edit_social_media/',edit_social_media.as_view(),name='edit_social_media'),
    path('profile_pic_change/',views.profile_pic_change,name='profile_pic_change'),
    path('apply_for_doctor/',views.apply_for_doctor,name='apply_for_doctor'),
    path('doctor_form/',views.doctor_form,name='doctor_form'),
    


    
    
  
]