from django.db import models
from django.forms.fields import EmailField

# FUNCTIONS ===============================================
def file_directory_path(instance, filename):
	return f"static/PLANTS/{filename}"
'''
def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename)
'''
# MODELS	=================================================
class Tierra(models.Model):
	'''
	Tipos de TIERRA
	'''
	name=models.CharField(max_length=200, null=False, blank=False)
	image=models.ImageField(upload_to="media/LANDS/", null=True, blank=True)
	description=models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name
class Plant(models.Model):
	'''
	Tipos de PLANTAS
	'''
	name=models.CharField(max_length=200, null=False, blank=False)
	nameComun=models.CharField(max_length=200,null=True, blank=True)
	temperatura=models.CharField(max_length=20,null=True, blank=True)
	temperaturaExtrema=models.CharField(max_length=20,null=True, blank=True)
	image=models.ImageField(upload_to=file_directory_path, null=True, blank=True)
	riego=models.CharField(max_length=100,null=True, blank=True)
	tierra=models.ForeignKey('Tierra',on_delete=models.SET_NULL, null=True, blank=True)
	description=models.TextField(null=True, blank=True)
	cuidados=models.TextField(null=True, blank=True)
	consejos=models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name
'''
Formulario de contacto
'''
MOTIVOS=[
	('REC','Recomendación'),
	('PET','Petición'),
	('ERR','Error'),
]
class Contact(models.Model):
	name=models.CharField(max_length=200, null=True, blank=True)
	email=models.EmailField(max_length=254, null=False, blank=False)
	motivo=models.CharField(max_length=3,choices=MOTIVOS)
	msg=models.TextField(null=False, blank=False)