from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^browse/$', 'browse.views.index'),
    (r'^browse/beers/$', 'browse.views.beers'),
    (r'^browse/breweries/$', 'browse.views.brewery'),
    (r'^browse/styles/$', 'browse.views.style'),
    (r'^browse/categories/$', 'browse.views.category'),
    (r'^user/(\w+)/$', 'account.views.user'),
    (r'^login/$', 'account.views.login'),
    (r'^browse/beer/(\d+)/$', 'browse.views.beer'),

    # Example:
    # (r'^Hopulent/', include('Hopulent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
