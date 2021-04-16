
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ratings, name='ratings'),
    path('/search', views.search, name="ratings_search"),
]
