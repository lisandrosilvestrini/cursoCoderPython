from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoriaForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()

class ItemsForm(forms.Form):
    title = forms.CharField()
    price = forms.DecimalField()
    description = forms.CharField()

class user_signup(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username","email","first_name", "last_name", "password1", "password2"]
        