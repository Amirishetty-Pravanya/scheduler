from django import http
from datetime import date
from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ChemistryClass
from bookings.models import bookings
from django.contrib.auth.models import User,auth
from accounts.models import UserDetails
from django.conf import settings                                                                                                                                                       
from twilio.rest import Client
# Create your views here.
def che(request):
    
    che=ChemistryClass.objects.all()
    curdate=date.today()
    curtime=datetime.now().time()
    return render(request,'chemistry.html',{'che':che,'curdate':curdate, 'curtime':curtime})

def book2(request):
    count=0
    classno=request.POST['classno']
    slotno=request.POST['slotno']
    name=request.POST['name']
    print(classno)
    print(slotno)
    p=ChemistryClass.objects.all()
    b=bookings.objects.all()
    u=UserDetails.objects.all()
    current_user = request.user 
    for ph in p:
        print(ph.classno, " ", classno)
        print(ph.slotno)
        if(int(classno)==int(ph.classno) and int(slotno)==int(ph.slotno)):
            date=ph.date
            time=ph.time
            mindose=ph.mindose
            allstu=ph.allstu
            break
        else:
            print("No")
    for boo in b:
        if(int(classno) ==int(classno) and str(boo.date)==str(date) and str(time)==str(time)):
            count=count+1
    
    if(count>=allstu):
        return HttpResponse("Class Limit exceeded. Book next class")
    for boo in b:
        if(int(boo.classno)==int(classno) and str(boo.username) == str(name) and str(boo.sub)=="chemistry"):
            return render(request,"same.html")
        if(str(boo.time)==str(time) and str(boo.username) == str(name) and str(boo.date)==str(date)):
            return render(request,"time.html")
    print(current_user.id, " user id")
    for us in u:
        if(int(us.user_id)==int(current_user.id)):
            dose1=us.dose1
            dose2=us.dose2
            phone=us.contactno
    if int(mindose)==1:
        if dose1:
            bo=bookings(username=name,classno=classno,sub="chemistry",date=date,time=time)
            bo.save()
        else:
            return HttpResponse("Vaccinate 1st Dose to book class")
    else:
        if dose2:
            bo=bookings(username=name,classno=classno,sub="chemistry",date=date,time=time)
            bo.save()
        else:
            return render(request,"d1.html")


        
    message_to_broadcast = ("Your slot on "+str(date)+ " class no "+ str(classno)+" of chemistry has been booked")
    client = Client("AC781a6124e645245f10e146457d688b63","c0bcb7a7fc55e2c80f089d055e256f72")
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to='+91'+str(phone),
                                   from_='+17175239533',
                                   body=message_to_broadcast)
    return render(request,"result.html")
    
    