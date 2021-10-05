
from django.contrib import admin
from django.urls import path
from .import views
from .models import statuscategory
from .models import statusdescription




urlpatterns = [
    path('',views.home.as_view(),name="home"),
    path('setting/',views.setting,name="setting"),
    path('signup/',views.signup,name="signup"),
    path('comments/<int:pk>',views.comments.as_view(),name='comments'),
    path('comments_for_feed/<int:pk>',views.comments_for_feed.as_view(),name='comments_for_feed'),
    path('edit/<int:pk>',views.edit.as_view(),name='edit'),
    path('post/<int:pk>/delete',views.delete.as_view(),name='delete'),
    path('comment/<int:pk>/delete',views.delete_comment.as_view(),name='delete_comment'),
    path('post/<int:pk>/share',views.share.as_view(),name='share'),
    path('report/',views.report,name='report'),
    path('search/',views.search,name='search'),
    path('feed/',views.feed.as_view(),name='feed'),
    path('notification/',views.notification.as_view(),name='notification'),
    path('notification/',views.notification.as_view(),name='notification'),
    path('social_media_form/',views.social_media_form,name='social_media_form'),
    path('post_profile/<int:pk>',views.post_profile.as_view(),name="post_profile"),
    path('doctor_profile/<int:pk>',views.doctor_profile.as_view(),name="doctor_profile"),
    path('feedback/',views.feedback,name="feedback"),
    path('feedback_form/',views.feedback_form,name='feedback_form'),
    path('buy_me_a_coffee/',views.buy_me_a_coffee,name='buy_me_a_coffee'),
    path('contact/',views.contact,name='contact'),
    path('contact_form/',views.contact_form,name='contact_form'),
    path('about/',views.about,name='about'),
    path('feed_form/',views.feed_form,name='feed_form'),
    path('shop/',views.shop,name='shop'),
    path('doctor_category/',views.doctor_category.as_view(),name='doctor_category'),
    
    
]