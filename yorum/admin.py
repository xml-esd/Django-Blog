from django.contrib import admin
from .models import Yorum

@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ["makale","yorum_yapan","yorum_tarih","yorum_içerik"]
    list_display_links = ["makale","yorum_yapan","yorum_tarih","yorum_tarih"]
    class Meta:
        model = Yorum
