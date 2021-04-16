
from django.contrib import admin
from django.urls import path
from . import views
from .views import ChartData, AreaChartData


urlpatterns = [
    path('', views.g_home, name='g_home'),
    path('complaint_stats/', views.complaint_stats, name='complaint_stats'),
    path('g_area_wise_graph/', views.g_area_wise_graph, name="g_area_wise_graph"),
    path('g_complaints/', views.complaints_list, name='g_complaints'),
    path('complaint_stats/chart/data/', ChartData.as_view()),
    path('area_wise/area_chart/data/', AreaChartData.as_view()),
    path('delete/<int:id>/', views.g_complaints_delete, name='g_complaint_delete'),
    path('area_wise/', views.area_wise, name='area_wise'),
    path('g_map', views.g_map, name='g_map'),
    path('g_track_complaint/<int:id>/',
         views.g_track_complaint, name='g_track_complaint'),
    path('g_view_complaint/<int:id>/',
         views.g_view_complaint, name='g_view_complaint'),
    path('block/<int:id>/<int:c_id>/', views.block, name='block_user'),
    #     path('ratings', views.ratings, name='g_ratings'),
    path('search', views.search, name='g_search'),
    path('ratings', views.ratings, name='ratings'),
    path('ratings/search', views.rating_search, name="ratings_search"),
]
