from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin

from tmster.engine.views import search, student, survey, view_student, autocomp

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',

	url(r'^$', 'direct_to_template', {'template':'home.html'}),

	url(r'^login/$', 'direct_to_template', {'template':'login.html'}),
	url(r'^logout/$', logout, {'next_page' : '/'}),

	url(r'^home/$', 'direct_to_template', {'template':'logued.html'}),

	url(r'^facebook/', include('django_facebook.urls')),

	url(r'^student/add/$',student, name ="add student"),

	#url(r'^student/(?P<studentID>\d+)/(?P<student_name>[a-zA-Z0-9_+-]+)/$', view_student, name='view student'),
	url(r'^student/(?P<studentID>\d+)/$', view_student, name='view student'),

	url(r'^search/$', search, name='search service'),
	url(r'^search/autocomplete/$',autocomp, name ="autocomp"),

	url(r'^survey/add/(?P<studentID>\d+)/$',survey, name ="add student"),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
