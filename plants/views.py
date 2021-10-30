# RENDER
from typing import ContextManager
from django.shortcuts import render, redirect
from .models import *
from .forms import *
#==========================================================
# WEBS
def home(request):
	return render(request, "home.html")
def plants(request):
	context={"title_":"CATÁLOGO"}
	context.update({"plants_":Plant.objects.all()})
	return render(request, "plants.html", context=context)
def about(request):
	context={"title_":	"ABOUT"}
	return render(request, "plants.html", context=context)
def userDashboard(request):
	# Sesión iniciada
	if request.user.is_authenticated:
		context={"title_": "PROFILE",}
		form=UserForm(request.POST or None)
		if form.is_valid():
			# instance=form.save(commit=False)
			print("================")
			print(form.cleaned_data)
			# print(_form.cleaned_data.get("name"))
		context.update({'form_': form})
			
		return render(request, "registration/profile.html", context=context)
	# Si se accede a PROFILE y no ha iniciado sesión.
	return redirect("/accounts/login/")
#----------------------------------------------------------