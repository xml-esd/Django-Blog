from django.contrib import admin
from django.urls import path
from yorum import views
app_name = "yorum"


urlpatterns = [
 
    path('', views.yorumekle,name="yorum"),
    


 
]