from django.urls import path,include
from yorum.api.views import yorum_list,yorum_detay

app_name = "yorum"
urlpatterns = [
    path('yorum/',yorum_list),
    path('yorum/detay/<int:id>/',yorum_detay)
]
