from django.db import models

# Create your models here.
class Track(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(default='')

	def __str__(self):
		return self.title