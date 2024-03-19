
from django.urls import path,include
from posting import views

urlpatterns = [
   path('indexposting',views.index,name="index"),
   path('insert',views.insertData,name="insertData"),
]
