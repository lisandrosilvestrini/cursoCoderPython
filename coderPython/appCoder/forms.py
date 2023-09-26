from django import forms

class CategoriaForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()

class ItemsForm(forms.Form):
    title = forms.CharField()
    price = forms.DecimalField()
    description = forms.CharField()