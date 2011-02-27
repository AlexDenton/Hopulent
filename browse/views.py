from beer.models import Beer 
from brewery.models import Brewery
from category.models import Category
from style.models import Style

from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    list_of_latest_beers = Beer.objects.all().order_by('last_mod')[:3]
    return render_to_response('browse/index.html', {'list_of_latest_beers':
list_of_latest_beers})
    
def beers(request):
    list_of_beers = Beer.objects.all().order_by('name')
    list_of_breweries = Brewery.objects.all().order_by('name')
    return render_to_response('browse/beers.html', {'list_of_beers': list_of_beers, 'list_of_breweries': list_of_breweries})
    
def breweries(request):
     list_of_breweries = Brewery.objects.all().order_by('name')
     return render_to_response('browse/breweries.html', {'list_of_breweries': list_of_breweries})

def styles(request):
    list_of_styles = Style.objects.all().order_by('style_name')
    return render_to_response('browse/styles.html', {'list_of_styles': list_of_styles})

	
