# RENDER
# from typing import ContextManager
from unicodedata import name
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
#==========================================================
# WEBS
def home(request):
	context={"title_":"Bienvido al PLANETA de las plantas."}
	return render(request, "home.html", context=context)
def plants(request):
	context={"title_":"CATÁLOGO"}
	context.update({"plants_":Plant.objects.all()})
	return render(request, "plants.html", context=context)
def detail(request, _search):
	context={"title_":"DETALLE"}
	## ■ SEACHING
	## ✔ Nombre
	if len(Plant.objects.filter(name=_search))==1:
		context.update({"plants_":Plant.objects.filter(name=_search)})
	## 
	# ✔ Nombre Común
	elif len(Plant.objects.filter(nameComun=_search))==1:
		context.update({"plants_":Plant.objects.filter(nameComun=_search)})
	## ✖ No existe la planta
	else:
		context={"title_":"❌ ERROR ❌ No existe la planta."}
	return render(request, "detalle.html", context=context)
def about(request):
	context={"title_":"ABOUT"}
	return render(request, "about.html", context=context)
def contact(request):
	context={"title_":"CONTACTO"}
	form=ContactFormWEB(request.POST or None)
	context.update({'form_':form})
	if form.is_valid():
		form_data=form.cleaned_data
		Contact.objects.create(
			name=form_data.get('name'),
			email=form_data.get('email'),
			motivo=form_data.get('motivo'),
			msg=form_data.get('mensaje'))

		msg="{} ({})\n\n{}".format(
			form_data.get('name'),
			form_data.get('email'),
			form_data.get('mensaje'),
		)
		# """ 
		## (?) Envío de correo deshabilitado, para las pruebas.
		send_mail(
			"Plantnet 🌿 "+form_data.get('motivo'),					# Asunto
			msg,																						# Cuerpo del mensaje
			settings.EMAIL_HOST_USER,												#
			[settings.EMAIL_HOST_USER],											# To
			fail_silently=False
		) 
		# """

		context.update({'send_':"✔ Mensaje enviado"})
		return render(request, "contact.html", context=context)
	return render(request, "contact.html", context=context)
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
		context.update({'form_':form})

		return render(request, "registration/profile.html", context=context)
	# Si se accede a PROFILE y no ha iniciado sesión.
	return redirect("/accounts/login/")
#----------------------------------------------------------