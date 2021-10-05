from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

def signinn(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password incorrect')

    

    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already taken")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                login(request,user)
                return redirect('/')
                
                
                
            
        else:
            messages.error(request, 'Password not matched')
    
    return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect ("/")


