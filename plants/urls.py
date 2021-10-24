from django.urls import path
from . import views

urlpatterns=[
	path('',				views.home,		name="home"),
	path('plants/',	views.plants,	name="plants"),
	path('about/',	views.about,	name="about"),
]