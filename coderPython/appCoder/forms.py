from django import forms

class CategoriaForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()