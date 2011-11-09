from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'campusconnect.clubs.views.homepage', name='home'),
    url(r'^major/$', 'campusconnect.clubs.views.major', name='major'),
    url(r'^major/(?P<major>[-\w]+)/$', 'campusconnect.clubs.views.major_detail', name='major_detail'),
    url(r'^college/$', 'campusconnect.clubs.views.college', name='college'),
    url(r'^college/(?P<college>[-\w]+)/$', 'campusconnect.clubs.views.college_detail', name='college_detail'),
    # url(r'^campusconnect/', include('campusconnect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
