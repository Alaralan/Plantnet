from django.urls import path
from . import views

urlpatterns=[
	path('',					views.home,						name="home"),
	path('plants/',		views.plants,					name="plants"),
	path('about/',		views.about,					name="about"),
	# path('login/',	views.login,					name="login"),
	# path('logout/',	views.logout,					name="logout"),
	path('accounts/profile/',	views.userDashboard,	name="profile"),
]