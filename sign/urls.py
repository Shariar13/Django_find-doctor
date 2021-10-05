from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('',views.signinn,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    
   
    
]