
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

from .models import Contact, Gallery

def index(request):
    return render(request,'login/index.html')


def about(request):
    photos=Gallery.objects.all()
    
    params={'photo':photos}

    return render(request,'login/about.html',params)

def contact(request):
    return render(request,'login/contact.html')

def loginuser(request):
    return render(request,'login/login.html')

def sign(request):
    return render(request,'login/signup.html')

def Contacthandle(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')

        querygen=Contact(name=name,email=email,phone=phone,message=message)
        querygen.save()
        messages.success(request,"your query is Submitted Successfully")
        return redirect('index')

    return HttpResponse('404 Not Found')





def Signuphandle(request):
    if request.method=="POST":
       
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['pass']
        confirm_pass=request.POST['confirm_pass']

        if len(name)>10 :
            messages.error(request,"username must be less than 10 characters")
            return redirect('sign')
        

        if password != confirm_pass:
            messages.error(request,"Password Do Not Matched")
            return redirect('sign')


        myuser = User.objects.create_user(name,email,password)
        myuser.save()
        messages.success(request,"Your Account Is Created Successfully")
        return redirect('index')

def loginhandle(request):
    if request.method=="POST":
        name=request.POST['name']
        login_pass=request.POST['login_pass']

        user = authenticate(request, username=name, password=login_pass)
        if user is not None:
            login(request, user)
            messages.success(request,"Welcome Back")
            return redirect('index')
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('loginuser')
   
    return HttpResponse ('404 NOt Found')

def logouthandle(request):
    logout(request)
    messages.success(request,"Logout Successfuly")
    return redirect('index')
   
