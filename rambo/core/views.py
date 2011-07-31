from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from core.api import *
from resources.models import *
from core.models import *
from django.template import RequestContext
from utils import * 
from django.contrib.auth import authenticate, login as do_login
from settings import LOGIN_REDIRECT_URL
try:
	import json
except:
	import simplejson as json

from django.contrib.auth.decorators import login_required
@login_required
def index(request):
	return render_to_response("index.html", {
		'get_user_resources':reverse("get_resources", kwargs={"user":request.user.username}),
		'get_shared_resources':reverse("get_shared_resources", kwargs={"user":request.user.username}),
	})

def login(request):
	if request.method == "GET":
		return render_to_response('login.html',{'next':request.REQUEST.get('next')},context_instance=RequestContext(request))
	if request.method == "POST":
		username = request.REQUEST.get('username', None)
		password = request.REQUEST.get('password', None)
		next = request.REQUEST.get('next', LOGIN_REDIRECT_URL)
		
		register = request.REQUEST.get('register', None)
		submit = request.REQUEST.get('submit', None)
		email = request.REQUEST.get('email', None)
		c_password = request.REQUEST.get('c_password', None)

		if register:
			if email and password == c_password:
				u = User.objects.create_user(username, email, password)
				u.save()
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						do_login(request, user)
						return HttpResponseRedirect(next)
			else:
				return render_to_response('login.html', {'error': 'passwords not matching'}, context_instance=RequestContext(request))
		elif submit:
			user = authenticate(username=username, password=password)	
			if user is not None:
				if user.is_active:
					do_login(request, user)
					return HttpResponseRedirect(next)
			
	return HttpResponseRedirect('/')


from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def add_booking(request, user, resource):
	data = {}
	data['description'] = request.REQUEST.get('description', '')
	data['date_start'] = request.REQUEST.get('date_start', None)
	data['date_end'] = request.REQUEST.get('date_end', None)
	data['time_start'] = request.REQUEST.get('time_start', None)
	data['time_end'] = request.REQUEST.get('time_end', None)
	data['repeat'] = False	
#	try:
	return response(do_book_resource(request.user, resource, data))
#	except Exception as e:
#		return error(str(e))

def del_booking(request, user, resource, booking):
	try:
		return response(do_unbook_resource(booking))
	except Exception as e:
		return error(str(e))

def get_booking(request,user, resource, booking):
	pass

def calendar(request, user, resource):
	if request.user.username == user:
		show_full=True
	else:
		conn = UserConnection.objects.filter(owner__username = user, target = request.user, shared_resource__slug = resource)
		if conn.count() != 1:
			raise Exception('wrong access')
		else:	
			show_full = conn[0].transparent_share
        format = request.REQUEST.get('format', 'json')
	start = None
	end = None
	if request.REQUEST.get('start', None):
                start = datetime.datetime.fromtimestamp(float(request.REQUEST.get('start', None)))
        if request.REQUEST.get('end', None):
                end = datetime.datetime.fromtimestamp(float(request.REQUEST.get('end', None)))

        ret = []
	print user
	print resource
	show_full = True
	r = Resource.objects.get(owner__username = user, slug = resource)
	query = Booking.objects.filter(resource = r)
        if start is not None and end is not None:
        	query = query.filter(date_start__lte=end, date_end__gte=start)
	for pa in query.all():
                ret.append({
	                'id':str(pa.id),
        	        'title':str(pa.description) if show_full else "",
                	'allDay':False,
	                'start': "%sT%sZ" % ( pa.date_start.isoformat(),pa.time_start.isoformat(), ),
        	        'end': "%sT%sZ" % ( pa.date_end.isoformat(),pa.time_end.isoformat(), ),
                	'editable': True,
        	        'description': pa.description,
                })
	if format=="json":
                return HttpResponse(json.dumps(ret))
	
