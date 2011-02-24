from browse.models import Beer
from browse.models import Brewer
from browse.models import Style
from browse.models import Category
from browse.models import BreweriesGeocode
from django.contrib import admin



admin.site.register(Beer)
admin.site.register(Brewer)
admin.site.register(Style)
admin.site.register(Category)
admin.site.register(BreweriesGeocode)
