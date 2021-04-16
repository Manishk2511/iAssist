
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.status, name='status'),
    path('<int:id>/', views.status_update, name='status_choice'),
    path('government/<int:id>/', views.g_status_update, name='g_status_choice'),

]
