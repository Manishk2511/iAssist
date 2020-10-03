
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='Insert_feedback'),
    path('list/', views.feedbackList, name='feedback_list'),
    path('<int:id>/', views.feedback, name='Update_feedback'),
    path('delete/<int:id>/', views.feedbackDelete, name='Delete_feedback')

]
