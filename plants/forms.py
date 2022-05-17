from django import forms
from django.forms import widgets
from .models import *
# ADMIN FORM ====================================
class PlantFormAdm(forms.ModelForm):
  class Meta:
    model =Plant
    fields=[
      "name",
      "nameComun",
      "temperatura",
      "temperaturaExtrema",
      "image",
      "riego",
      "tierra",
      "description",
      "cuidados",
      "consejos",
    ]
  ## Esta parte es para validar los datos antes de guardarlos en la BD.
  # def clean_riego(self):
  #   print(self.cleaned_data.get("riego"))
  #   _riego=self.cleaned_data.get("riego").strip()
  #   return _riego

# WEB FORM ======================================
class ContactFormWEB(forms.Form):
  name=forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
  
  email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Correo electrónico'}))
  motivo=forms.CharField(
    max_length=3,
    widget=forms.Select(choices=MOTIVOS)
  )
  mensaje=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Mensaje'}))
class UserForm(forms.Form):
  name=forms.CharField(max_length=200)
  surname=forms.CharField(max_length=200)
  email=forms.EmailField()
