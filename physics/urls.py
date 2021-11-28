from django.contrib import admin   
from django.urls import path
from . import views
urlpatterns = [
    path('', views.phy,name='phy'),
    path('book',views.book1,name='book1'),
    
]