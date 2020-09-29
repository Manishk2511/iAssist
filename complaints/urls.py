
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.complaints, name='complaints'),
    # get and post request for insert
    path('', views.complaints_form, name='complaint_insert'),
    # get and post request for retrieval
    path('list', views.complaints_list, name='list'),
    # get and post request for update
    path('<int:id>', views.complaints_form, name='complaint_update'),
    # get and post request for delete
    path('delete/<int:id>', views.complaints_delete, name='complaint_delete')
]
