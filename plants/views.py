from django.shortcuts import render

# Create your views here.
def home(request):
	variable="Hola Mundo"
	return render(request, "home.html", context={"variable": variable})