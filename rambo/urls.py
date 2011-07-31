from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'core.views.index', name='index'),
	url(r'^booking/', include('core.urls'), name="core_ep"),
	url(r'^login/$', 'core.views.login'),
	url(r'^logout/$', 'core.views.logout_view'),
	url(r'^res/', include('resources.urls'), name="resources_ep"),	
	url(r'^admin/', include(admin.site.urls)),
)
