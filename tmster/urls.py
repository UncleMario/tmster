from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin

from tmster.engine.views import student, survey

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',

	url(r'^$', 'direct_to_template', {'template':'home.html'}),
	url(r'^logout/$', logout, {'next_page' : '/'}),

	url(r'^facebook/', include('django_facebook.urls')),

	url(r'^student/add/$',student, name ="add student"),
	url(r'^survey/add/(?P<studentID>\d+)/$',survey, name ="add student"),




) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
