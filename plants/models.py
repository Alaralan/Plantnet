from django.db import models

# Create your models here.
def file_directory_path(instance, filename):
    return f"my_files/{instance.id}/{filename}"

class Plant(models.Model):
	name=models.CharField(max_length=200, null=False, blank=False)
	nameComun=models.CharField(max_length=200,null=True)
	description=models.TextField(null=True)
	image=models.ImageField(upload_to=file_directory_path, null=True)
	riego=models.IntegerField(null=True)
	tierra=models.CharField(
		max_length=3,
		choices=[
			('TIE',"Tierra"),
			('ARE',"Arenosa"),
			('ARC',"Arcillosa"),
			('LIM',"Limosa"),
			('TUB',"Turba"),
			('TIZ',"Tiza")
		],
		default='TIE'
	)

	def __str__(self):
		return self.name