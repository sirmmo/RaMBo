from django.db import models
from resources.models import *
from django.contrib.auth.models import User

class Booking(models.Model):
	user = models.ForeignKey(User)
	resource = models.ForeignKey(Resource)
	description = models.TextField()

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


