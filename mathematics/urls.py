from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.mat,name='mat'),
    path('bookmat',views.book3,name='book3')
]