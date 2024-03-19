from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('student_login/', views.student_login, name='student_login'),
    path('company_login/', views.company_login, name='company_login'),
]
