from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.che,name='che'),
    path('bookche',views.book2,name='book2')
]