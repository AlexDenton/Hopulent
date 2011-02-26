from browse.models import Beer
from browse.models import Breweries
from browse.models import BreweriesGeocode
from browse.models import Categories
from browse.models import Styles
from django.contrib import admin

admin.site.register(Beer)
admin.site.register(Breweries)
admin.site.register(BreweriesGeocode)
admin.site.register(Categories)
admin.site.register(Styles)
