from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	variable="Hola Mundo"
	return render(request, "home.html", context={"variable": variable})
def plants(request):
	_objetos=Plant.objects.all()
	return render(request, "plants.html", context={"plants":_objetos})
def about(request):
	return render(request, "about.html")
