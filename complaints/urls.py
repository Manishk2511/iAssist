
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.complaints_form, name='complaint_insert'),
    path('list/', views.complaints_list, name='list'),
    path('<int:id>/', views.complaints_form, name='complaint_update'),
    path('delete/<int:id>/', views.complaints_delete, name='complaint_delete'),
    path('track_complaint/<int:id>/',
         views.track_complaint, name='track_complaint'),
    path('view_complaint/<int:id>/',
         views.view_complaint, name='view_complaint'),
    path('otp', views.otp, name='otp'),
    path('onmap/<int:id>/', views.view_on_map, name='onmap'),
]
