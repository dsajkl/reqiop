from django.db import models

# Create your models here.
class ParentData(models.Model):

	ParentName = models.CharField(max_length = 255)
	ParentEmail = models.CharField(max_length = 255)
 	def __unicode__(self):
		return self.ParentEmail
