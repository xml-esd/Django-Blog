from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı :")
    password = forms.CharField(label="Şifre :",widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Adınız' , label="Ad")
    last_name = forms.CharField(max_length=30, required=True, help_text='Soyadınız' , label="Soyad")
    email = forms.EmailField(max_length=254, help_text='Email Adresiniz')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ContactForm(forms.Form):
    ad = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    mesaj = forms.CharField(widget=forms.Textarea,required=True)