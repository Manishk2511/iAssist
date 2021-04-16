
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('otp', views.otp, name='account_otp'),
]
