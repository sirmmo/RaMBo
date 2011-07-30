from utils import *
from resources.api import *

from django.contrib.auth.decorators import login_required

try:
	import json
except:
	import simplejson as json

@login_required
def get_resources(request, user=None):
	try:
		return response(do_get_resources(user))
	except Exception as e:
		return error(str(e))

@login_required
def get_resource(request, user, resource):
	try:
		return response(do_get_resource(user, resource))
	except Exception as e:
		return error(str(e))

@login_required
def add_resource(request):
	data = request.REQUEST.get('data', None)
	if data is None:
		return error("data must be set")
	data = json.loads(data)
	try:
		return response(do_add_resource(request.user.username, data))
	except Exception as e:
		return error(str(e))

@login_required
def remove_resource(request,user,  resource):
	try:
		return response(do_remove_resource(request.user, user, data))
	except Exception as e:
		return error(str(e))

@login_required
def op_category(request, op):
	name = request.REQUEST.get('name', None)
	if name is None:
		return error("name must be set")
	if op == "add":
		parent = request.REQUEST.get('parent', None)
#		try:
		return response(do_add_category(request.user, name, parent))
#		except Exception as e:
#			return error(str(e))
	elif op == "rm":
		try:
			return response(do_remove_category(request.user, name))
		except Exception as e:
			return error(str(e))
@login_required
def get_categories(request):
	try:
		return response(do_get_categories(request.user.username))
	except Exception as e:
		return error(str(e))

@login_required
def edit_category(request, category):
	pass
@login_required
def edit_resource(request,resource):
	pass


@login_required
def send_share_request(request, user):
        pass
@login_required
def respond_share_request(request):
        pass

@login_required
def get_shared_resources(request, user):
        pass

