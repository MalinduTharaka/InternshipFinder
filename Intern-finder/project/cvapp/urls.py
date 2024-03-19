from django.urls import path
from cvapp import views

urlpatterns = [
    path('cvindex', views.index, name="index"),
    path('about', views.about, name="about"),
    path('insertD', views.insertData, name="insertData"),
    path('mycv', views.mycv, name="mycv"),
    path('update/<int:cv_id>/', views.updateData, name='updateData'),
    path('delete/<int:cv_id>/', views.deleteData, name="deleteData"),
]
