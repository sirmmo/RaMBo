from django.db import models
from resources.models import *
from django.contrib.auth.models import User

class Booking(models.Model):
	resource = models.ForeignKey(Resource)
	date_start = models.DateField()
	date_end = models.DateField()

	time_start = models.TimeField()
	time_end = models.TimeField()

	REPETITION_CHOICES = (
		('d', 'Daily'),
		('w', 'Weekly'),
		('m', 'Monthly'),
	)

	repeat = models.CharField(max_length = 1, choices = REPETITION_CHOICES)

	
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
			

