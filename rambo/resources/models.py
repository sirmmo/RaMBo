from django.db import models

from django.contrib.admin.models import User
from django.template.defaultfilters import slugify

class ResourceCategory(models.Model):
	parent = models.ForeignKey('ResourceCategory')
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(blank=True, null=True, unique=True)
	
	def save(self, *args, **kwargs):
		slug = slugify(name)

	def __unicode__(self):
		return self.name

class Resource(models.Model):
	owner = models.ForeignKey(User)
	category=models.ForeignKey(ResourceCategory)
	name = models.CharField(max_length = 250)

	icon = models.ImageField(upload_to="icons")

	def __unicode__(self):
		return self.name
