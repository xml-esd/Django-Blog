from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField,CKEditorWidget


class Makale(models.Model):
    Yazar = models.ForeignKey("auth.User",on_delete = models.CASCADE) #Üye silinirse o üyeye ait herşeyi sil
    Başlık = models.CharField(max_length = 50)
    İçerik = RichTextField()
    Olusturma_Tarihi = models.DateTimeField(auto_now_add=True)  #True yaptık o anki tarihi alması için
    makal_resim = models.FileField(blank=True , null=True ,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.Başlık
    class Meta:
        ordering = ['-Olusturma_Tarihi', 'Yazar']

        