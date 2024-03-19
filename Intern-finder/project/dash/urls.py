from django.contrib import admin
from django.urls import path,include
from dash import views
from django.conf import settings

urlpatterns = [
    path('indexx/<str:username>/', views.indexx, name='indexx'),
    path('apply',views.apply,name="apply"),
    path('apply/',views.apply_job, name='apply_job'),


]
