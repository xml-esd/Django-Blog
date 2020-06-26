from django import forms
from .models import Makale
class MakaleForm(forms.ModelForm):
    İçerik = forms.Textarea()
    class Meta:
        model = Makale
        fields = ["Başlık","İçerik","makal_resim"]