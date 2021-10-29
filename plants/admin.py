from django.contrib import admin
from .models import *

# Aquí se modifica 

'''
Modifica el display en el apartado administración (/admin/)
'''
class aPlants(admin.ModelAdmin):
  list_display=["__str__","nameComun","riego","tierra","image"]
  list_editable=["nameComun","tierra","riego"]
  search_fields=["name","nameComun"]
  class Meta:
    model=Plant
class aTierra(admin.ModelAdmin):
  list_display=["__str__","image"]
'''
Modelos que apareceran.
'''
admin.site.register(Plant, aPlants)
admin.site.register(Tierra, aTierra)