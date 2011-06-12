from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'index.views.main_page'),
    (r'^browse/$', 'browse.views.index'),
    (r'^browse/beers/$', 'browse.views.beers'),
    (r'^browse/breweries/$', 'browse.views.breweries'),
    (r'^browse/breweries/(\d+)/$', 'browse.views.brewerydetail'),
    (r'^browse/styles/$', 'browse.views.styles'),
    (r'^browse/styles/(\d+)/$', 'browse.views.stylesdetail'),
    (r'^browse/location/$', 'browse.views.location'),
    (r'^browse/location/(\w+)/$', 'browse.views.locationdetail'),
    (r'^signin/$', 'account.views.signin'),
    (r'^signout/$', 'account.views.signout'),
    (r'^beer/(\d+)/$', 'beer.views.beer'),
    (r'^brewery/(\d+)/$', 'brewery.views.brewery'),
    (r'^aboutus/$', 'aboutus.views.index'),
    (r'^learn/$', 'learn.views.index'),
    (r'^learn/beers/$', 'learn.views.beers'),
    (r'^learn/ingredients/$', 'learn.views.ingredients'),
    (r'^learn/glassware/$', 'learn.views.glassware'),
    (r'^learn/rating/$', 'learn.views.rating'),
    (r'^contribute/$', 'contribute.views.index'),
    (r'^search/$', 'search.views.search'),
    (r'^style/(\d+)/$', 'style.views.style'),
    (r'^signup/$', 'account.views.signup'),
    (r'^account/userprofile/(\d+)/$', 'account.views.user_profile'),
    (r'^account/editprofile/(\d+)/$', 'account.views.edit_profile'),
    (r'^account/fileupload/(\d+)/$', 'account.views.directupload'), 
    #t Example:
    # (r'^Hopulent/', include('Hopulent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
