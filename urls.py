from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('campusconnect.clubs.views',
    # Examples:
    url(r'^$', 'homepage', name='home'),
    url(r'^major/$', 'major', name='major'),
    url(r'^major/(?P<major_slug>[-\w]+)/$', 'major_detail', name='major_detail'),
    url(r'^college/$', 'college', name='college'),
    url(r'^college/(?P<college_slug>[-\w]+)/$', 'college_detail', name='college_detail'),
    url(r'^club/$', 'club', name='club'),
    url(r'^club/(?P<club>[-\w]+)/$', 'club_detail', name='club_detail'),
    url(r'^question/$', 'question', name='question'),
    url(r'^question/(?P<question>[-\w]+)/$', 'question_detail', name='question_detail'),
    # url(r'^campusconnect/', include('campusconnect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
