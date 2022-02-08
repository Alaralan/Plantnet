from django.conf.urls import url, include
# from django.urls import path
from . import views

urlpatterns=[
	url(r'^$',									views.home,						name="home"),
	url(r'^plants/',						views.plants,					name="plants"),
	url(r'^about/',							views.about,					name="about"),
	url(r'^contact/',						views.contact,				name="contact"),
	url(r'^accounts/',					include('registration.backends.default.urls')),
	url(r'^accounts/profile/',	views.userDashboard,	name="profile"),
]