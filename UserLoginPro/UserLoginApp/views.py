from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

# Create your views here.
def registartion(request):
    if request.method == 'POST':
        rname = request.POST.get("name")
        remail = request.POST.get("email")
        rpassword = request.POST.get("password")
        rconfirmpassword = request.POST.get("confirmpassword")
        if rpassword != rconfirmpassword:
            return HttpResponse('Password is not matched')
        else:
            user_1 = User.objects.create_user(rname,remail,rpassword)
            user_1.save()
            return redirect(login)
    return render(request,'registration.html')
def login1(request):
    if request.method == 'POST':
        rname = request.POST.get("name")
        rpassword = request.POST.get("password")
        user_auth = authenticate(request,username = rname,password = rpassword)
        if user_auth is not None:
            login(request,user_auth)
            return redirect(home)
        else:
            return HttpResponse('Invalid user')
        
    return render(request,'login.html')

@login_required(login_url='log')
def home(request):
    return render(request,'home.html')

def logout1(request):
    logout(request)
    return redirect(login1)