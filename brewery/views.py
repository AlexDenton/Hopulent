from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from brewery.models import Brewery
from beer.models import Beer

def brewery(request, brewery_id):
	brewery = get_object_or_404(Brewery, pk=brewery_id)
	list_of_beers = Beer.objects.filter(brewery=brewery.id)
	return render_to_response(
		'brewery/brewery.html', 
		{'brewery': brewery, 'list_of_beers': list_of_beers},
		context_instance=RequestContext(request)
	)
