from django.db import models

from django.contrib.admin.models import User
from django.template.defaultfilters import slugify

from django.core.urlresolvers import reverse

class ResourceCategory(models.Model):
	parent = models.ForeignKey('ResourceCategory', null=True, default=None)
	name = models.CharField(max_length=250)
	slug = models.SlugField(blank=True, null=True, unique=True)
	
	def save(self, *args, **kwargs):
		slug = slugify(self.name)

	def __unicode__(self):
		return self.name

class Resource(models.Model):
	owner = models.ForeignKey(User)
	category=models.ForeignKey(ResourceCategory)
	name = models.CharField(max_length = 250)

	icon = models.ImageField(upload_to="icons")

	def __unicode__(self):
		return self.name
	def url(self):
		return reverse('get_resource', kwargs={'user':self.owner.username, 'name':self.name})
	class Meta:
		unique_together= ('owner', 'name')

class ResourceProperty(models.Model):
	name = models.CharField(max_length=250)
	value=models.CharField(max_length=250)

	resource = models.ForeignKey(Resource, related_name="properties")

	def __unicode__(self):
		return "%s.%s = %s" % (self.resource, self.name, self.value)


class UserConnection(models.Model):
        owner = models.ForeignKey(User, related_name="sharing")
        target = models.ForeignKey(User, related_name ="shared")

        shared_resources = models.ManyToManyField(Resource)

        def __unicode__(self):
                return "%s => %s [%s]" % (self.requester, self.owner, ", ".join(self.shared_resources.all()))

class ConnectionRequest(models.Model):
        requester = models.ForeignKey(User, related_name="requests_sent")
        owner = models.ForeignKey(User, related_name="requests_to_answer")

        def accept(self, resources):
                u = UserConnection()
                u.owner = self.owner
                u.target = self.requester
                u.save()
                for resource in resources :
                        u.shared_resources.add(Resource.objects.get(id=resource))
                        u.save()

                self.remove()

        def refuse(self):
                self.remove()

        def ignore(self):
                pass

        def __unicode__(self):
                return "%s => %s" % (self.requester, self.owner)
