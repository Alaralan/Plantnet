# RENDER
# from typing import ContextManager
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
#==========================================================
# WEBS
def home(request):
	return render(request, "home.html")
def plants(request):
	context={"title_":"CATÁLOGO"}
	context.update({"plants_":Plant.objects.all()})
	return render(request, "plants.html", context=context)
def about(request):
	context={"title_":"ABOUT"}
	return render(request, "plants.html", context=context)
def contact(request):
	context={"title_":"CONTACT"}
	form=ContactFormWEB(request.POST or None)
	context.update({'form_':form})
	if form.is_valid():
		form_data=form.cleaned_data
		Contact.objects.create(
			name=form_data.get('name'),
			email=form_data.get('email'),
			motivo=form_data.get('motivo'),
			msg=form_data.get('mensaje'))
		context.update({'ok_':"Mensaje enviado"})

		msg="{} ({})\n\n{}".format(
			form_data.get('name'),
			form_data.get('email'),
			form_data.get('mensaje'),
		)
		send_mail(
			"Plantnet 🌿 "+form_data.get('motivo'),					# Asunto
			msg,																						# Cuerpo del mensaje
			settings.EMAIL_HOST_USER,												# From
			[settings.EMAIL_HOST_USER],											# To
			fail_silently=False
		)
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