from django.contrib import admin

from .models import Makale




@admin.register(Makale) #Admin paneline makaleleri görebilmek için kaydettik
class MakaleAdmin(admin.ModelAdmin):
    list_display = ["Başlık","Yazar","Olusturma_Tarihi"]
    list_display_links = ["Başlık","Yazar","Olusturma_Tarihi"] #yazar bilgisine , basliga ve tarihe link verdik.
    list_filter = ["Başlık","Olusturma_Tarihi"] #filtreledik
    search_fields = ["Başlık"] #makalenin basligina göre bir arama yapmamızı sağlıyor
    class Meta: #Django tarafından yapılan bir class özel bir class model ile makaleyi birbirine bağladık
        model = Makale


