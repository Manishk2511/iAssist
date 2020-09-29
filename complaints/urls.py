
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.complaints_form, name='complaint_insert'),
    path('list/', views.complaints_list, name='list'),
    path('<int:id>/', views.complaints_form, name='complaint_update'),
    path('delete/<int:id>/', views.complaints_delete, name='complaint_delete')
]
