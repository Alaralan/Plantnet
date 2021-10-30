from django.contrib import admin
from .models import *
from .forms import *

# Aquí se modifica 

'''
Modifica el display en el apartado administración (/admin/)
'''
class aPlants(admin.ModelAdmin):
  list_display=["__str__","nameComun","riego","tierra","image"]
  list_editable=["nameComun","tierra","riego"]
  search_fields=["name","nameComun"]
  # Formulario personalizado `forms.py`. Utili para validar los datos.
  form=PlantForm
  # Formulario autogenerado por DJANGO.
  # class Meta:
    # model=Plant
class aTierra(admin.ModelAdmin):
  list_display=["__str__","image"]
'''
Modelos que apareceran.
'''
admin.site.register(Plant, aPlants)
admin.site.register(Tierra, aTierra)