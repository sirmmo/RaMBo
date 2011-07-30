from django.http import HttpResponse

from utils import * 

try:
	import json
except:
	import simplejson as json

def index(request):
	return HttpResponse("index")

# Create your views here.

def add_booking(request):

	data = request.REQUEST.get('booking_data', None)
	data = json.loads(data)
	try:
		return response(do_book_resource(request.user, resource, data))
	except Exception as e:
		return error(str(e))

def remove_booking(request, booking):
	try:
		return response(do_unbook_resource(booking))
	except Exception as e:
		return error(str(e))
		

