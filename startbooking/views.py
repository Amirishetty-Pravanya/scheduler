from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def beginbooking(request):
    return render(request,'startbooking.html')
