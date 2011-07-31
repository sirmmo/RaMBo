from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from utils import * 

try:
	import json
except:
	import simplejson as json

def index(request):
	return render_to_response("index.html", {
		'get_user_resources':reverse("get_resources", kwargs={"user":request.user.username}),
		'get_shared_resources':reverse("get_shared_resources", kwargs={"user":request.user.username}),
	})

def register(request):
	pass	

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
		

