from django import forms
from django.forms import widgets
from .models import *

## ADMIN FORM
class PlantFormAdm(forms.ModelForm):
  class Meta:
    model =Plant
    fields=["name","nameComun","description","image","riego","tierra"]
  def clean_riego(self):
    _riego=self.cleaned_data.get("riego")
    if _riego<0:
      raise forms.ValidationError("❌ RIEGO ❌ No puede ser negativo")
    return _riego
## WEB FORM
'''
class PlantFormWeb(forms.Form):
  name=forms.CharField(max_length=200)
  nameComun=forms.CharField(max_length=200)
  description=forms.Textarea()
  image=forms.ImageField()
  riego=forms.IntegerField()
  # tierra=forms.InlineForeignKeyField(Tierra)
'''
class ContactFormWEB(forms.Form):
  name=forms.CharField(max_length=200, required=False)
  email=forms.EmailField()
  motivo=forms.CharField(
    max_length=3,
    widget=forms.Select(choices=MOTIVOS)
  )
  mensaje=forms.CharField(widget=forms.Textarea)
  
class UserForm(forms.Form):
  name=forms.CharField(max_length=200)
  surname=forms.CharField(max_length=200)
  email=forms.EmailField()
