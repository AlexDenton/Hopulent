from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.main_page'),
    (r'^browse/$', 'browse.views.index'),
    (r'^browse/beers/$', 'browse.views.beers'),
    (r'^browse/breweries/$', 'browse.views.breweries'),
    #(r'^browse/styles/$', 'browse.views.styles'),
    #(r'^browse/categories/$', 'browse.views.categories'),
    (r'^user/(\w+)/$', 'account.views.user'),
    (r'^login/$', 'account.views.loginify', {'username': 'username', 'password': 'password'}),
    (r'^beer/(\d+)/$', 'beer.views.beer'),
    (r'^brewery/(\d+)/$', 'brewery.views.brewery'),
    #(r'category/(\d+)/$', 'category.views.category'),
    #(r'style/(\d+)/$', 'style.views.style'), 

    # Example:
    # (r'^Hopulent/', include('Hopulent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
