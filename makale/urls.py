from django.contrib import admin
from django.urls import path
from makale import views
from yorum import views as y_views
app_name = "makale"


urlpatterns = [
    path('makalekle/', views.makalekle,name="makalekle"),
    path('makaleayrinti/<int:id>', views.ayrinti,name="makaleayrinti"),
    path('makaleguncelle/<int:id>', views.makaleguncelle,name="makaleguncelle"),
    path('makalesil/<int:id>', views.makalesil,name="makalesil"),
    path('makaleler/', views.makaleler,name="makaleler"),
    path('yorum/<int:id>', y_views.yorumekle,name="yorum"),
    


 
]