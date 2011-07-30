from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'core.views.index', name='index'),
	url(r'^booking/', include('core.urls'), name="core_ep"),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^res/', include('resources.urls'), name="resources_ep"),	
	url(r'^admin/', include(admin.site.urls)),
)
