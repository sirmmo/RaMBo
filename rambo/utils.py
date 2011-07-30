from django.http import *

try:
	import json
except:
	import simplejson as json

def __message(msg, msg_t):
	return HttpResponse(json.dumps({'type':msg_t, 'content':msg}))

def response(msg):
	return __message(msg, "response")

def error(msg):
	return __message(msg, "error")


