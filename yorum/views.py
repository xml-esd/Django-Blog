from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from makale.models import Makale
from django.contrib import messages
from .models import Yorum



def yorumekle(request,id):
    makale = get_object_or_404(Makale,id=id)

    if request.method == "POST":
        yorum_yapan = request.POST.get("yorum_yapan",request.user.username)
        yorum_içerik = request.POST.get("yorum_içerik")
        
        yeniYorum = Yorum(yorum_yapan = yorum_yapan , yorum_içerik = yorum_içerik)
        yeniYorum.makale = makale
        yeniYorum.save()
    return redirect(reverse("makale:makaleayrinti",kwargs={"id":id}))
