from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'r/add$', 'resources.views.add_resource', name='add_resource'),
	url(r'r/(?P<user>\w+)/(?P<resource>\w+)$', 'resources.views.get_resource', name='get_resource'),
	url(r'r/(?P<user>\w+)$', 'resources.views.get_resources', name='get_resources'),
)
