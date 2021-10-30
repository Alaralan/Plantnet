from django import forms
from .models import *

# Cambia el fomulario para el panel ADMIN
class PlantForm(forms.ModelForm):
  class Meta:
    model =Plant
    fields=["name","nameComun","description","image","riego","tierra"]
  def clean_riego(self):
    _riego=self.cleaned_data.get("riego")
    if _riego<0:
      raise forms.ValidationError("❌ RIEGO ❌ No puede ser negativo")
    return _riego

class UserForm(forms.Form):
  name=forms.CharField(max_length=100)
  surname=forms.CharField(max_length=200)
  email=forms.EmailField()
