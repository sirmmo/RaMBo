from django.db import models
from django.contrib.admin.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class ResourceCategory(models.Model):
	parent = models.ForeignKey('ResourceCategory', null=True,blank=True, default=None)
	name = models.CharField(max_length=250)
	slug = models.SlugField(blank=True, null=True, unique=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(ResourceCategory, self).save(self, *args, **kwargs)

	def __unicode__(self):
		return self.name

class Resource(models.Model):
	owner = models.ForeignKey(User)
	category=models.ForeignKey(ResourceCategory)
	name = models.CharField(max_length = 250)
	slug = models.SlugField(blank=True, null=True, unique=True)
	icon = models.ImageField(upload_to="icons")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Resource, self).save(self, *args, **kwargs)	

	def __unicode__(self):
		return self.name
	def url(self):
		kwa = {'user':self.owner.username, 'name':self.name}
		return reverse('get_resource',args=[],kwargs={'user':self.owner.username, 'resource':self.slug})
	def share(self):
		return reverse('share_resource', args=[], kwargs={'user':self.owner.username, 'resource':self.slug})
	class Meta:
		unique_together= ('owner', 'slug')

class UserConnection(models.Model):
        owner = models.ForeignKey(User, related_name="sharing")
        target = models.ForeignKey(User, related_name ="shared")
        shared_resource = models.ForeignKey(Resource,related_name="shared_by")
	transparent_share = models.BooleanField(default=False)
        def __unicode__(self):
                return "%s => %s [%s]" % (self.owner, self.target, self.shared_resource)
