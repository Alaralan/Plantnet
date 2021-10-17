from django.db import models

# Create your models here.
def file_directory_path(instance, filename):
    return f"my_files/{instance.id}/{filename}"

class Plant(models.Model):
	name=models.CharField(max_length=200, null=False, blank=False)
	description=models.TextField(null=True)
	image=models.ImageField(upload_to=file_directory_path, null=True)
	riego=models.IntegerField(null=True)

	def __str__(self):
		return self.name