from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^(?P<link_id>\w+)/$', 'view_qr', name='view_qr'),
)
