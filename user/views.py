from django.shortcuts import render,redirect,HttpResponse
from .forms import SignUpForm,LoginForm,ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from makale.models import Makale
from django.core.mail import send_mail



def register(request):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Başarıyla kayıt olundu {username}!')
            return redirect('index')
        
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
    

def loginUser(request):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request,"Kullanıcı Adı Veya Parola Hatalı")
            return render(request,"login.html",context)
        login(request,user)    
        return redirect("index")
    
    
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,f'Başarıyla Çıkış Yaptınız {request.user.username}')
    return redirect("index")
def profil(request):
    arama = request.GET.get("arama")
    if arama:
        makaleler = Makale.objects.filter(Başlık__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleler})
    fullname =  request.user.get_full_name()
    makale = Makale.objects.filter(Yazar = request.user)
    context = {'fullname':fullname,'makaleler':makale}
    return render(request,"profil.html",context)
def iletisim(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['ad']
            sender_email = form.cleaned_data['email']

            message = "{0} Sana yeni bir mesaj gönderdi:\n\n MESAJ : {1}\n Gönderen mail : {2}".format(sender_name, form.cleaned_data['mesaj'],form.cleaned_data['email'])
            send_mail('DevBlog iletişim', message, sender_email, ['gorkerem23@gmail.com'])
            messages.warning(request,'Mesaj içeriğiniz Admine iletilmiştir.')
            return redirect("index")

    else:
        form = ContactForm()
        

    return render(request, 'iletisim.html', {'form': form})
