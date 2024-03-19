from django.urls import path
from . import views

urlpatterns = [
    path('company_list', views.company_list, name='company_list'),
    path('createc/', views.company_create, name='company_create'),
    path('<int:company_id>/update/', views.company_update, name='company_update'),
    path('<int:company_id>/delete/', views.company_delete, name='company_delete'),
]
