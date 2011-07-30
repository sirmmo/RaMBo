from core.models import *
from django.contrib.auth.models import User

def do_book_resource(user, booking_data):
	
	b= Booking(**booking_data)
	b.save()

	return b.id

def do_unbook_resource(booking):
	Booking.filter(id=booking).remove()


