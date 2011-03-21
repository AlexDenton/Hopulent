from beer.models import Beer 
from brewery.models import Brewery
from category.models import Category
from style.models import Style

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    list_of_latest_beers = Beer.objects.all().order_by('last_mod')[:3]
    return render_to_response(
    		'browse/index.html', 
    		{'list_of_latest_beers': list_of_latest_beers}, 
    		context_instance=RequestContext(request)
    )
    
def beers(request):
    list_of_beers = Beer.objects.all().order_by('name')
    list_of_breweries = Brewery.objects.all().order_by('name')
    return render_to_response(
    		'browse/beers.html', 
    		{'list_of_beers': list_of_beers, 'list_of_breweries': list_of_breweries},
    		context_instance=RequestContext(request)
    )
    
def breweries(request):
     list_of_breweries = Brewery.objects.all().order_by('name')
     return render_to_response(
     	'browse/breweries.html', 
     	{'list_of_breweries': list_of_breweries},
     	context_instance=RequestContext(request)
     )

def brewerydetail(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    list_of_beers = Beer.objects.filter(brewery=brewery.id)
    return render_to_response(
    		'browse/brewerydetail.html', 
    		{'brewery': brewery, 'list_of_beers': list_of_beers},
    		context_instance=RequestContext(request)
    	)

def styles(request):
    list_of_styles = Style.objects.distinct().order_by('style_name')
    return render_to_response(
    		'browse/styles.html', 
    		{'list_of_styles': list_of_styles},
    		context_instance=RequestContext(request)
    	)

def styledetail(request, style_id):
	style = get_object_or_404(Style, pk=style_id)
	list_of_beers = Beer.objects.filter(style_id=style.id)
	return render_to_response(
		'browse/styledetail.html', 
		{'style': style, 'list_of_beers': list_of_beers},
		context_instance=RequestContext(request)
	)

def categories(request):
	list_of_categories = Category.objects.all().order_by('cat_name')
	return render_to_response(
		'browse/categories.html', 
		{'list_of_categories':list_of_categories},
		context_instance=RequestContext(request)
	)

def location(request):
	list_of_locations = Brewery.objects.values_list('state', flat=True).distinct().filter(country='United States').order_by('state')
	return render_to_response(
		'browse/location.html', 
		{'list_of_locations':list_of_locations},
		context_instance=RequestContext(request)
	)

def locationdetail(request, state):
	list_of_beers = Beer.objects.filter(beer.brewery.state, pk=state)
	return render_to_response('browse/locationdetail.html', 
				{'list_of_beers': list_of_beers},	 				 context_instance=RequestContext(request))
