from django.urls import path
from . import views

urlpatterns = [
    path('student_list', views.student_list, name='student_list'),
    path('creates/', views.student_create, name='student_create'),
    path('<str:stu_nic>/updatest/', views.student_update, name='student_update'),
    path('<str:stu_nic>/deleteST/', views.student_delete, name='student_delete'),
]
