from core.models import *
from django.contrib.auth.models import User

def do_book_resource(user,resource, booking_data):
	
	b= Booking()
	b.user = User.objects.get(username = user)
	b.resource = Resource.objects.get(owner__username = user, slug = resource)
	b.description = booking_data['description']
	b.date_start = booking_data['date_start']
	b.date_end = booking_data['date_end']
	b.time_start = booking_data['time_start']
	b.time_end = booking_data['time_end']
	b.repeat = booking_data['repeat']	
	b.save()

	return b.id

def do_unbook_resource(booking):
	Booking.filter(id=booking).remove()


