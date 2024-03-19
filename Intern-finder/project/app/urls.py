
from django.urls import path,include
from django.contrib import admin
from app import views
from .views import index

urlpatterns = [    
    path('indexapp/<str:username>/', views.index, name='indexapp'),
    path('insert/<str:username>/', index, name='insert'),
    path('viewcv/<str:nic>/', views.view_cv, name='view_cv'),

]