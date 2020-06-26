from rest_framework.serializers import ModelSerializer
from yorum.models import Yorum
from rest_framework import serializers



class YorumOlusturSerializer(ModelSerializer):
    makale_baslik = serializers.CharField(source='makale.Başlık', read_only=True)
    makale_id = serializers.CharField(source='makale.id', read_only=True)
    yorum_yapan = serializers.CharField(source="yorum.yorum_yapan",read_only=True)
    class Meta:
        model = Yorum
        fields = ('id','yorum_yapan','yorum_içerik','makale_baslik','makale_id','yorum_tarih')
    

class YorumGetirSerializer(ModelSerializer):
    makale_baslik = serializers.CharField(source='makale.Başlık', read_only=True)
    class Meta:
        model = Yorum
        fields = ('id','yorum_yapan','yorum_içerik','yorum_tarih','makale','makale_baslik')




        

