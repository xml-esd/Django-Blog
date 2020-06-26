from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import MakaleForm
from django.contrib import messages
from .models import Makale
from yorum.views import Yorum
from yorum.models import Yorum
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.html import conditional_escape
# Create your views here.
def makaleler(request):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    makaleler = Makale.objects.all()
    return render(request,"makaleler.html",{"makaleler":makaleler})
def index(request):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    makaleler = Makale.objects.all()[:1]
    return render(request,"index.html",{"makaleler":makaleler})
def about(request):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    return render(request,"about.html")
def makalekle(request,auto_escape=True):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler},auto_escape=auto_escape)
    form = MakaleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        makale = form.save(commit=False)
        makale.Yazar = request.user #Giriş yapan kullanıcının kullanıcı adını yazar olarak aldık.
        makale.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("user:profil")
    return render(request,"makalekle.html",{"form":form})
def ayrinti(request,id):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    #makale = Makale.objects.filter(id = id).first()
    #Aşağıdaki kodda httpresponse sınıfını kullanarak try catch ile özelleştirilen 404.html sayfasına yönlendirdik.
    try:
        makale = Makale.objects.get(id=id)
    except Makale.DoesNotExist:
        return render(request,"404.html")
    yorumlar = makale.yorumlar.all()
    return render(request,"makaleayrinti.html",{"makale":makale,"yorumlar":yorumlar})

def makaleguncelle(request,id):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    makale = get_object_or_404(Makale,id=id)
    form = MakaleForm(request.POST or None , request.FILES or None,instance = makale)
    if form.is_valid():
        makale = form.save(commit=False)
        makale.Yazar = request.user #Giriş yapan kullanıcının kullanıcı adını yazar olarak aldık.
        makale.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("user:profil")
    return render(request,"makaleguncelle.html",{"form":form})
    
def makalesil(request,id):
    makale = get_object_or_404(Makale,id=id)
    makale.delete()
    messages.success(request,"Makaleniz Başarıyla Silindi.")
    return redirect("user:profil")
