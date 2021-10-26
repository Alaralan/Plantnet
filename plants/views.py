# RENDER
from django.shortcuts import render, redirect
from .models import *
# LOGIN
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
#==========================================================
# WEBS
def home(request):
	return render(request, "home.html")
def plants(request):
	_title="CATÁLOGO"
	_objetos=Plant.objects.all()
	return render(request, "plants.html", context={
		"plants":	_objetos,
		"title_":	_title
	})
def about(request):
	_title="ABOUT"
	return render(request, "about.html", context={"title_":	_title})
def userDashboard(request):
	_title="PROFILE"
	if request.user.is_authenticated:
		return render(request, "registration/profile.html", context={"title_":	_title})
	# Si se accede a PROFILE y no ha iniciado sesión.
	return redirect("/accounts/login/")
#----------------------------------------------------------
# FUNCIONES
# * Al utilizar "auth" incluido en python no es necesario
# def login(request):
# 	_title="Login"
# 	form = AuthenticationForm()
# 	if request.method == "POST":
# 		form = AuthenticationForm(data=request.POST)
# 		if form.is_valid():
# 			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
# 			if user is not None:
# 				do_login(request, user)
# 				return redirect("/user/")
# 	return render(request, "login.html", {'form': form}, context={"title_":	_title})
# def logout(request):
# 	_title="Logout"
# 	if request.user.is_authenticated:
# 		do_logout(request)
# 		return render(request, "logout.html", context={"title_":	_title})
# 	return redirect("/")