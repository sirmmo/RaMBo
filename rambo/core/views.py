from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from core.api import *
from resources.models import *
from core.models import *

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

def add_booking(request, user, resource):

	if request.method == "GET":
		return render_to_response('form.html')
	else:
		data = request.REQUEST.get('booking_data', None)
	
		if data:
			data = json.loads(data)
		try:
			return response(do_book_resource(request.user, resource, data))
		except Exception as e:
			return error(str(e))

def del_booking(request, user, resource, booking):
	try:
		return response(do_unbook_resource(booking))
	except Exception as e:
		return error(str(e))

def get_booking(request,user, resource, booking):
	pass

def calendar(request, user, resource):
        format = request.REQUEST.get('format', 'json')
	start = None
	end = None
	if request.REQUEST.get('start', None):
                start = datetime.datetime.fromtimestamp(float(request.REQUEST.get('start', None)))
                print "start", start
        if request.REQUEST.get('end', None):
                end = datetime.datetime.fromtimestamp(float(request.REQUEST.get('end', None)))
                print "end", end

        ret = []
	print user
	print resource
	r = Resource.objects.get(owner__username = user, slug = resource)
	query = Booking.objects.filter(resource = r)
        if start is not None and end is not None:
        	query = query.filter(day__lte=end, day__gte=start)
	for pa in query.all():
                ret.append({
	                'id':str(pa.id),
        	        'title':str(pa.description),
                	'allDay':False,
	                'start': "%sT%sZ" % ( pa.date_start.isoformat(),pa.time_start.isoformat(), ),
        	        'end': "%sT%sZ" % ( pa.date_end.isoformat(),pa.time_end.isoformat(), ),
                	'editable': True,
        	        'description': pa.description,
                })
	if format=="json":
                return HttpResponse(json.dumps(ret))
	
