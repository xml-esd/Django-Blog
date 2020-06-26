from django.db import models
from makale.models import Makale

class Yorum(models.Model):
    makale = models.ForeignKey(Makale , on_delete = models.CASCADE , verbose_name="Makale",related_name="yorumlar")
    yorum_yapan = models.CharField(max_length=50,verbose_name="isim")    
    yorum_içerik = models.CharField(max_length=200,verbose_name="yorum")
    yorum_tarih = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-yorum_tarih', 'yorum_yapan']
