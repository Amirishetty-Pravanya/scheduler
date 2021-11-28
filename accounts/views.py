from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http.response import HttpResponse 
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import UserDetails
# Create your views here.

def login(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = auth.authenticate(username=username,password=password)

         if user is not None:
              auth.login(request,user)
              return redirect('home/')
         else:
              messages.info(request,'INVALID CREDENTIALS')
              return redirect('login')
    else:
         return render(request,'login.html')


def register(request):
     first_name = request.POST.get('first_name')
     last_name = request.POST.get('last_name')
     username = request.POST.get('username')
     password1 = request.POST.get('password1')
     password2 = request.POST.get('password2')
     contact = request.POST.get('contact')   
     email = request.POST.get('email')
     dose1=request.POST.get('dose1')
     dose2=request.POST.get('dose2')
     if request.method == 'POST':
        if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'USERNAME TAKEN')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'EMAIL TAKEN')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    userdetails=UserDetails(contactno=contact, dose1=dose1,dose2=dose2,user_id=user.id)
                    userdetails.save()
                    print('User created')
                    return redirect('login')
        else:
                print('password not matching')
                return redirect('register')
     else:
        return render(request,'register.html')



def logout(request):
     auth.logout(request)
     return redirect('home/')
