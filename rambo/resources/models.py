from django.db import models

class ResourceCategory(models.Model):
	parent = models.ForeignKey('ResourceCategory')
	name = models.CharField(unique=True)
	slug = models.SlugField(blank=True, null=True)

class Resource(models.Model):
	category=models.ForeignKey(ResourceCategory)
	name = models.CharField(max_length = 250)


