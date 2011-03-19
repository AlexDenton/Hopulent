from beer.models import Beer 
from brewery.models import Brewery
from category.models import Category
from style.models import Style

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    list_of_latest_beers = Beer.objects.all().order_by('last_mod')[:3]
    return render_to_response('browse/index.html', {'list_of_latest_beers': list_of_latest_beers}, context_instance=RequestContext(request))
    
def beers(request):
    list_of_beers = Beer.objects.all().order_by('name')
    list_of_breweries = Brewery.objects.all().order_by('name')
    return render_to_response('browse/beers.html', {'list_of_beers': list_of_beers, 'list_of_breweries': list_of_breweries})
    
def breweries(request):
     list_of_breweries = Brewery.objects.all().order_by('name')
     return render_to_response('browse/breweries.html', {'list_of_breweries': list_of_breweries})

def brewerydetail(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    list_of_beers = Beer.objects.filter(brewery_id=brewery.id)
    return render_to_response('browse/brewerydetail.html', {'brewery': brewery, 'list_of_beers': list_of_beers})

def styles(request):
    list_of_styles = Style.objects.all().order_by('style_name')
    return render_to_response('browse/styles.html', {'list_of_styles': list_of_styles})

def styledetail(request, style_id):
	style = get_object_or_404(Style, pk=style_id)
	list_of_beers = Beer.objects.filter(style_id=style.id)
<<<<<<< HEAD
	list_of_breweries = Brewery.objects.all().order_by('name')
	return render_to_response('browse/styledetail.html', {'style': style, 'list_of_beers':
list_of_beers, 'list_of_breweries': list_of_breweries})
=======
	return render_to_response(
		'browse/styledetail.html', 
		{'style': style, 'list_of_beers': list_of_beers} 'list_of_breweries': list_of_breweries}
	)
>>>>>>> 286bfc3b6dee294b57de15c5b8849ec09f3f00a0

def categories(request):
	list_of_categories = Category.objects.all().order_by('cat_name')
	return render_to_response('browse/categories.html', {'list_of_categories':
list_of_categories})

def location(request):
	list_of_locations = Brewery.objects.values('state').distinct().order_by('state')
	return render_to_response('browse/location.html', {'list_of_locations':
list_of_locations})

def locationdetail(request, state):
	brewery = get_object_or_404(Brewery, pk=state)
	list_of_breweries = Brewery.objects.filter(state=brewery.state)
	for brewery in list_of_breweries:
		list_of_beers = Beer.objects.filter(brewery_id=brewery.id)
	return render_to_response('browse/locationdetail.html', {'list_of_beers': list_of_beers})
