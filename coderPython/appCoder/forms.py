from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from appCoder.models import *
from django.forms import ModelForm, ValidationError


class CategoriaForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()

# class ItemsForm(forms.Form):
#     title = forms.CharField()
#     price = forms.DecimalField()
#     description = forms.CharField()
#     image = forms.ImageField()
#     category = forms.

class ItemsForm(ModelForm):

    class Meta:
        model = Item
        fields = ["title","price","description","created_date","condition","image","category"]
    
    image = forms.FileField(label="Imagen")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Categ.objects.all()
    
    def clean_image(self):
        image = self.cleaned_data["image"]
        if not image:
            raise ValidationError("Debes seleccionar una imagen")
        return image

class user_signup(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username","email","first_name", "last_name", "password1", "password2"]

class updateForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email","first_name", "last_name", "password1", "password2"]

class avatarForm(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]
