from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'r/add$', 'resources.views.add_resource', name='add_resource'),
	url(r'r/add/template$', 'resources.views.add_resource_template', name='add_resource_template'),
#	url(r'r/add/form$', 'resources.views.add_resourcei_form', name='add_resource_form'),
	url(r'r/(?P<user>\w+)/(?P<resource>\w+)$', 'resources.views.get_resource', name='get_resource'),
	url(r'r/(?P<user>\w+)/(?P<resource>\w+)/remove$', 'resources.views.remove_resource', name='remove_resource'),
	url(r'r/(?P<user>\w+)$', 'resources.views.get_resources', name='get_resources'),
	url(r's/(?P<user>\w+)$', 'resources.views.get_shared_resources', name="get_shared_resources"),
	url(r'c$', 'resources.views.get_categories', name="get_categories"),
	url(r'c/add$', 'resources.views.op_category',{'op':'add'}, name="add_category"),
	url(r'c/remove$', 'resources.views.op_category',{'op':'rm'}, name="remove_category"),
)
