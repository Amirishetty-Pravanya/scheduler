from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def signin(request):
    return redirect('/login')
def signup(request):
    return redirect('/register')
def logout(request):
     auth.logout(request)
     return redirect('/home/')
