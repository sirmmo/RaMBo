from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#	url(r'r/add$', 'core.views.add_resource', name='add_resource'),
	url(r'^(?P<user>\w+)/(?P<resource>[\w-]+)$', 'core.views.calendar', name='booking_url'),
	url(r'^(?P<user>\w+)/(?P<resource>[\w-]+)/add$', 'core.views.add_booking', name='add_booking'),
	url(r'^(?P<user>\w+)/(?P<resource>[\w-]+)/(?P<booking>\d+)$', 'core.views.get_booking', name='get_booking'),
	url(r'^(?P<user>\w+)/(?P<resource>[\w-]+)/(?P<booking>\d+)/remove$', 'core.views.del_booking', name='del_booking'),
#	url(r'r/(?P<user>\w+)$', 'core.views.get_resources', name='get_resources'),
)
