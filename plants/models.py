from django.db import models

# FUNCTIONS =========================================================
def file_directory_path(instance, filename):
	return f"IMG/PLANTS/{filename}"
''' 
def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename) 
'''
# MODELS	===========================================================
class Tierra(models.Model):
	'''
	Tipos de TIERRA
	'''
	name=models.CharField(max_length=200, null=False, blank=False)
	image=models.ImageField(upload_to="IMG/LANDS/", null=True, blank=True)
	description=models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name
class Plant(models.Model):
	''' 
	Tipos de PLANTAS
	'''
	name=models.CharField(max_length=200, null=False, blank=False)
	nameComun=models.CharField(max_length=200,null=True, blank=True)
	description=models.TextField(null=True, blank=True)
	image=models.ImageField(upload_to=file_directory_path, null=True, blank=True)
	riego=models.IntegerField(null=True, blank=True)
	tierra=models.ForeignKey('Tierra',on_delete=models.SET_NULL, null=True, blank=True)
	def __str__(self):
		return self.name