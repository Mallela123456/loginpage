from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.registartion,name='reg'),
    path('login/', views.login1,name='log'),
    path('logout/', views.logout1,name='logout'),
    path('home/', views.home,name='home'),
]